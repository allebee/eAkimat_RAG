"""PDF loader — extracts text and images, chunks content for ChromaDB."""

from __future__ import annotations

import logging
import re
from collections import Counter
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

import fitz  # PyMuPDF
from PIL import Image

from app.config import settings

logger = logging.getLogger(__name__)

# --- Screenshot filtering ---
# The instruction PDFs embed three kinds of images, and across the 29 files only
# ~32% of them are actual screenshots:
#   1. page-header logos, redrawn on every page (~40% of the image stream)
#   2. tiny inline glyphs — button icons sitting inside a sentence (~28%)
#   3. real UI screenshots — the only ones worth showing the user
# Ingestion used to keep all three and hand them out to "Рис. X.Y" references by
# list index, so the first two figure references on every page were served the
# header logos and every real screenshot landed under the wrong step.
HEADER_PAGE_RATIO = 0.5      # same image on >= half the pages => header/watermark
HEADER_MIN_PAGES = 3         # ...but only for documents long enough to tell
MIN_FIGURE_HEIGHT_PT = 40.0  # rendered height; inline glyphs are ~10-25pt
MIN_FIGURE_WIDTH_PT = 60.0
MIN_IMAGE_BYTES = 2048       # guards against blank/solid-colour rectangles

# --- Topic normalization map ---
# Maps Russian topic names (from Excel / filenames) to normalized keys
TOPIC_NORMALIZE: Dict[str, str] = {
    "штатное расписание": "staffing",
    "штатное": "staffing",
    "форма расчетов": "calculation_forms",
    "формы расчетов": "calculation_forms",
    "краткая инструкция по заполнению форм расчетов": "calculation_forms",
    "свод по абп": "svod_abp_gu_gkkp",
    "свод по абп/гу/гккп": "svod_abp_gu_gkkp",
    "свод по абп и гу": "svod_abp_gu_gkkp",
    "свод по абп, гу, гккп": "svod_abp_gu_gkkp",
    "форма гу": "forma_gu",
    "лимиты": "limits",
    "лимиты расходы": "limits_expenses",
    "лимиты доходы": "limits_income",
    "лимиты нормативы распределения": "limits_distribution",
    "лимиты гу гккп": "limits_gu_gkkp",
    "бип": "bip",
    "бюджетные инвестиционные проекты": "bip",
    "бюджетные программы": "budget_programs",
    "формирование доходной части": "income_formation",
    "формирование расходной части": "expense_formation",
    "подписанты": "signatories",
    "оценка проектов": "project_evaluation",
    "методика оценки": "evaluation_methodology",
    "расходы развития": "development_expenses",
    "медиамониторинг": "media_monitoring",
    "сводные отчеты": "consolidated_reports",
    "заявки гу": "gu_requests",
    "справки": "references",
    "корректировка расходы": "correction_expenses",
    "корректировка доходы": "correction_income",
    "уточнение расходы": "refinement_expenses",
    "уточнение доходы": "refinement_income",
    "индивидуальный план финансирования": "ipf",
    "взаимоувязка целевых индикаторов": "target_indicators",
    "регистрационные данные и права доступа": "registration_access",
    "сэп": "sep",
    "сэм": "sem",
    "потребности снп": "snp_needs",
}


def normalize_topic(title: str) -> str:
    """Normalize a PDF title to a topic key."""
    title_lower = title.lower().strip()
    # Try exact match first
    for pattern, normalized in TOPIC_NORMALIZE.items():
        if pattern in title_lower:
            return normalized
    # Fallback: slugify
    slug = re.sub(r"[^\w\s]", "", title_lower)
    slug = re.sub(r"\s+", "_", slug.strip())
    return slug[:50]


def derive_regime(title: str) -> str:
    """Guess the regime from the PDF title."""
    title_lower = title.lower()
    execution_keywords = ["исполнение", "ипф", "индивидуальный план", "справки", "заявки на внесение"]
    for kw in execution_keywords:
        if kw in title_lower:
            return "budget_execution"
    if "медиамониторинг" in title_lower:
        return "media_monitoring"
    return "budget_planning"


def derive_module(topic: str) -> str:
    """Derive the module from a normalized topic."""
    module_map = {
        "limits": "limits",
        "limits_expenses": "limits",
        "limits_income": "limits",
        "limits_distribution": "limits",
        "limits_gu_gkkp": "limits",
        "ipf": "formation",
        "income_formation": "formation",
        "expense_formation": "formation",
        "media_monitoring": "media_monitoring",
        "signatories": "signatories",
        "registration_access": "administration",
    }
    return module_map.get(topic, "budget_requests")


class PDFLoader:
    """Extracts text and images from a PDF, then chunks for ChromaDB."""

    def __init__(self, chunk_size: int = 800, chunk_overlap: int = 200):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        settings.images_path.mkdir(parents=True, exist_ok=True)

    def load_pdf(
        self,
        pdf_path: str,
        title: Optional[str] = None,
    ) -> List[Dict[str, Any]]:
        """Process a single PDF into chunked documents ready for ChromaDB.

        Returns a list of dicts with 'id', 'content', and 'metadata'.
        """
        path = Path(pdf_path)
        if not path.exists():
            logger.error("PDF not found: %s", pdf_path)
            return []

        if title is None:
            from app.ingestion.deduplicator import extract_clean_title
            title = extract_clean_title(path.name)

        topic = normalize_topic(title)
        regime = derive_regime(title)
        module = derive_module(topic)

        logger.info("Processing PDF: '%s' → topic=%s, regime=%s", title, topic, regime)

        doc = fitz.open(str(path))
        all_text = ""
        images_extracted: List[Dict[str, Any]] = []
        page_count = len(doc)
        repeated_xrefs = self._find_repeated_xrefs(doc)

        for page_num in range(page_count):
            page = doc[page_num]
            page_text, page_images = self._extract_page(
                page, page_num + 1, path.stem, repeated_xrefs
            )
            all_text += f"\n\n--- Страница {page_num + 1} ---\n\n{page_text}"
            images_extracted.extend(page_images)

        doc.close()

        # Chunk the full text
        chunks = self._chunk_text(all_text)
        logger.info("  Extracted %d pages, %d images, %d chunks", page_count, len(images_extracted), len(chunks))

        # Build ChromaDB documents
        documents: List[Dict[str, Any]] = []
        file_slug = re.sub(r"[^\w]", "_", path.stem)[:30]

        for i, chunk_text in enumerate(chunks):
            # Find images that belong to this chunk's page range
            chunk_image_url = self._find_chunk_image(chunk_text, images_extracted)

            doc_id = f"pdf_{file_slug}_chunk_{i:04d}"
            documents.append(
                {
                    "id": doc_id,
                    "content": chunk_text,
                    "metadata": {
                        "type": "instruction",
                        "topic": topic,
                        "module": module,
                        "regime": regime,
                        "source_page": f"page_{regime.split('_')[0]}_{topic.split('_')[0]}",
                        "source_file": path.name,
                        "chunk_index": i,
                        "language": "ru",
                        "image_url": chunk_image_url,
                        "video_url": "",
                    },
                }
            )

        return documents

    @staticmethod
    def _find_repeated_xrefs(doc: fitz.Document) -> Set[int]:
        """Images drawn on most pages — page headers, footers, watermarks.

        These carry no instructional content but dominate the image stream, so
        they must never be offered as a step's screenshot.
        """
        page_count = len(doc)
        if page_count < HEADER_MIN_PAGES:
            return set()

        counts: Counter = Counter()
        for page in doc:
            for xref in {img[0] for img in page.get_images(full=True)}:
                counts[xref] += 1

        threshold = max(HEADER_MIN_PAGES, page_count * HEADER_PAGE_RATIO)
        return {xref for xref, seen_on in counts.items() if seen_on >= threshold}

    def _extract_page(
        self,
        page: fitz.Page,
        page_num: int,
        pdf_stem: str,
        repeated_xrefs: Set[int],
    ) -> Tuple[str, List[Dict[str, Any]]]:
        """Extract a page's text and screenshots, interleaved in reading order.

        Screenshots are placed by their position on the page rather than paired
        with "Рис. X.Y" references by list index: PDF resource order does not
        follow the layout, and headers/glyphs shift the pairing anyway. Laying
        text blocks and images out by coordinate puts each [IMAGE:] marker where
        the screenshot actually sits — after the step that introduces it and
        before its "Рис. X.Y" caption.
        """
        # Where each image is really drawn (get_images order is resource order).
        bbox_by_xref: Dict[int, Any] = {}
        for info in page.get_image_info(xrefs=True):
            xref = info.get("xref")
            if xref and xref not in bbox_by_xref:
                bbox_by_xref[xref] = info.get("bbox")

        images: List[Dict[str, Any]] = []
        # Page layout items as (y0, x0, text) — text blocks and image markers.
        items: List[Tuple[float, float, str]] = []

        for img_idx, img_info in enumerate(page.get_images(full=True), 1):
            xref = img_info[0]
            if xref in repeated_xrefs:
                continue  # header logo / watermark

            bbox = bbox_by_xref.get(xref)
            if bbox is None:
                continue  # referenced but not drawn on this page

            width, height = bbox[2] - bbox[0], bbox[3] - bbox[1]
            if height < MIN_FIGURE_HEIGHT_PT or width < MIN_FIGURE_WIDTH_PT:
                continue  # inline button glyph, not a screenshot

            try:
                base_image = page.parent.extract_image(xref)
            except Exception as exc:
                logger.debug("Failed to extract image %d from page %d: %s", img_idx, page_num, exc)
                continue
            if not base_image or not base_image.get("image"):
                continue

            data = base_image["image"]
            if len(data) < MIN_IMAGE_BYTES:
                continue

            img_filename = f"{pdf_stem}_page{page_num}_img{img_idx}.jpeg"
            img_path = settings.images_path / img_filename
            with open(img_path, "wb") as f:
                f.write(data)

            images.append(
                {
                    "filename": img_filename,
                    "page": page_num,
                    "path": str(img_path),
                }
            )
            items.append((bbox[1], bbox[0], f"[IMAGE: {img_filename}]"))

        for block in page.get_text("blocks"):
            if block[6] != 0:  # not a text block
                continue
            text = block[4].strip()
            if text:
                items.append((block[1], block[0], text))

        items.sort(key=lambda item: (item[0], item[1]))
        page_text = "\n".join(text for _, _, text in items)

        return page_text, images

    def _chunk_text(self, text: str) -> List[str]:
        """Split text into overlapping chunks by character count."""
        if len(text) <= self.chunk_size:
            return [text.strip()] if text.strip() else []

        chunks: List[str] = []
        start = 0
        while start < len(text):
            end = start + self.chunk_size

            # Try to break at a paragraph or sentence boundary
            if end < len(text):
                # Look for paragraph break
                newline_pos = text.rfind("\n\n", start + self.chunk_size // 2, end)
                if newline_pos > start:
                    end = newline_pos + 1
                else:
                    # Look for sentence break
                    period_pos = text.rfind(". ", start + self.chunk_size // 2, end)
                    if period_pos > start:
                        end = period_pos + 2

            chunk = text[start:end].strip()
            if chunk:
                chunks.append(chunk)

            # Move forward with overlap
            start = end - self.chunk_overlap if end < len(text) else end

        return chunks

    def _find_chunk_image(
        self, chunk_text: str, images: List[Dict[str, Any]]
    ) -> Optional[str]:
        """Check if any image marker exists in the chunk text."""
        for img in images:
            if img["filename"] in chunk_text:
                return img["filename"]
        return None
