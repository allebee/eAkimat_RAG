"""PDF deduplication utility — removes duplicate PDFs by content hash."""

from __future__ import annotations

import hashlib
import logging
import re
from pathlib import Path
from typing import Dict, List, Tuple

logger = logging.getLogger(__name__)


def compute_file_hash(filepath: Path) -> str:
    """Compute SHA256 hash of file contents."""
    sha256 = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            sha256.update(chunk)
    return sha256.hexdigest()


def extract_clean_title(filename: str) -> str:
    """Extract a clean title from the PDF filename.

    Input:  '1727762648104-Инструкция_«Штатное_расписание»_30.09.24.pdf'
    Output: 'Инструкция Штатное расписание 30.09.24'
    """
    # Remove leading timestamp
    name = re.sub(r"^\d{13}-", "", filename)
    # Remove extension
    name = re.sub(r"\.pdf$", "", name, flags=re.IGNORECASE)
    # Replace underscores with spaces
    name = name.replace("_", " ")
    # Remove special chars but keep Cyrillic, Latin, digits, dots, spaces
    name = re.sub(r"[«»()\"']", "", name)
    return name.strip()


def deduplicate_pdfs(pdf_dir: Path) -> List[Dict[str, str]]:
    """Find unique PDFs by content hash, keeping the latest version of each.

    Returns a list of dicts with keys: path, hash, title, filename.
    Duplicates are logged but not included.
    """
    pdf_files = sorted(pdf_dir.glob("*.pdf"))
    if not pdf_files:
        logger.warning("No PDF files found in %s", pdf_dir)
        return []

    logger.info("Found %d PDF files in %s", len(pdf_files), pdf_dir)

    # Group by content hash
    hash_groups: Dict[str, List[Path]] = {}
    for pdf_path in pdf_files:
        file_hash = compute_file_hash(pdf_path)
        hash_groups.setdefault(file_hash, []).append(pdf_path)

    # Keep latest (highest timestamp prefix) per hash group
    unique_pdfs: List[Dict[str, str]] = []
    total_dupes = 0

    for file_hash, paths in hash_groups.items():
        # Sort by filename (timestamp prefix) — last = newest
        paths.sort(key=lambda p: p.name)
        latest = paths[-1]
        dupes = len(paths) - 1
        total_dupes += dupes

        unique_pdfs.append(
            {
                "path": str(latest),
                "hash": file_hash,
                "title": extract_clean_title(latest.name),
                "filename": latest.name,
            }
        )

        if dupes > 0:
            logger.info(
                "  '%s': kept latest, removed %d duplicate(s)",
                extract_clean_title(latest.name),
                dupes,
            )

    logger.info(
        "Deduplication complete: %d unique / %d total (%d duplicates removed)",
        len(unique_pdfs),
        len(pdf_files),
        total_dupes,
    )
    return unique_pdfs
