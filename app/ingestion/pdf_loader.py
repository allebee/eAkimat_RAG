"""PDF loader — extracts text and images, chunks content for ChromaDB."""

from __future__ import annotations

import logging
import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import fitz  # PyMuPDF
from PIL import Image

from app.config import settings

logger = logging.getLogger(__name__)

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

        for page_num in range(page_count):
            page = doc[page_num]
            page_text, page_images = self._extract_page(page, page_num + 1, path.stem)
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

    def _extract_page(
        self, page: fitz.Page, page_num: int, pdf_stem: str
    ) -> Tuple[str, List[Dict[str, Any]]]:
        """Extract text and images from a single page."""
        # Get text blocks with positions
        blocks = page.get_text("blocks")
        # Sort by vertical position (y0)
        sorted_blocks = sorted(blocks, key=lambda b: (b[1], b[0]))

        text_parts: List[str] = []
        images: List[Dict[str, Any]] = []

        # Extract images
        image_list = page.get_images(full=True)
        for img_idx, img_info in enumerate(image_list, 1):
            try:
                xref = img_info[0]
                base_image = page.parent.extract_image(xref)
                if base_image and base_image.get("image"):
                    img_filename = f"{pdf_stem}_page{page_num}_img{img_idx}.jpeg"
                    img_path = settings.images_path / img_filename
                    with open(img_path, "wb") as f:
                        f.write(base_image["image"])
                    images.append(
                        {
                            "filename": img_filename,
                            "page": page_num,
                            "path": str(img_path),
                        }
                    )
            except Exception as exc:
                logger.debug("Failed to extract image %d from page %d: %s", img_idx, page_num, exc)

        # Build text from blocks
        for block in sorted_blocks:
            if block[6] == 0:  # Text block
                text = block[4].strip()
                if text:
                    text_parts.append(text)

        page_text = "\n".join(text_parts)

        # Smart image placement: insert [IMAGE:] right after "Рис." references
        # Pattern matches "Рис. X.Y", "рис. X.Y", "Рисунок X"
        fig_pattern = re.compile(r"((?:Рис(?:унок)?\.?\s*\d[\d.]*[^\n]*))", re.IGNORECASE)
        fig_matches = list(fig_pattern.finditer(page_text))

        used_images: set = set()
        if fig_matches and images:
            # Assign images to figure references in order
            for i, match in enumerate(fig_matches):
                if i < len(images):
                    img = images[i]
                    marker = f"\n[IMAGE: {img['filename']}]"
                    # Insert marker right after the figure reference
                    insert_pos = match.end()
                    page_text = page_text[:insert_pos] + marker + page_text[insert_pos:]
                    used_images.add(i)
                    # Adjust positions for subsequent matches (offset by marker length)
                    offset = len(marker)
                    fig_matches = list(fig_pattern.finditer(page_text))

        # Append remaining images that couldn't be matched to figure refs
        for i, img in enumerate(images):
            if i not in used_images:
                page_text += f"\n[IMAGE: {img['filename']}]"

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
