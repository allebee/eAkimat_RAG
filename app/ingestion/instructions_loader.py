"""Instructions loader — reads instructions.xlsx and builds navigation tree."""

from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Any, Dict, List, Optional

import openpyxl

logger = logging.getLogger(__name__)


def load_instructions(instructions_path: str) -> List[Dict[str, Any]]:
    """Load instructions.xlsx, expand merged cells, and build flat list.

    The Excel uses merged cells (empty values inherit from above).
    This function fills forward to reconstruct the hierarchy.

    Returns a list of instruction entries with full hierarchy + video URL.
    """
    path = Path(instructions_path)
    if not path.exists():
        logger.error("Instructions file not found: %s", instructions_path)
        return []

    wb = openpyxl.load_workbook(str(path), read_only=True)
    ws = wb.active
    if ws is None:
        return []

    # Expected columns: [index], Режим, Модуль, Раздел, Подраздел, URL
    entries: List[Dict[str, Any]] = []
    prev_regime = ""
    prev_module = ""
    prev_section = ""

    for row in ws.iter_rows(min_row=2, values_only=True):
        row_list = list(row)
        if len(row_list) < 6:
            continue

        _, regime, module, section, subsection, url = row_list

        # Fill forward from previous row (handle merged cells)
        regime = str(regime).strip() if regime else prev_regime
        module = str(module).strip() if module else prev_module
        section = str(section).strip() if section else prev_section
        subsection = str(subsection).strip() if subsection else ""
        url = str(url).strip() if url else ""

        prev_regime = regime
        prev_module = module
        prev_section = section

        if url:
            entries.append(
                {
                    "regime": regime,
                    "module": module,
                    "section": section,
                    "subsection": subsection,
                    "video_url": url,
                }
            )

    wb.close()
    logger.info("Loaded %d instruction entries from %s", len(entries), instructions_path)
    return entries


def build_navigation_tree(entries: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Build a hierarchical navigation tree from flat instruction entries.

    Output structure:
    {
        "Бюджетное планирование": {
            "Лимиты": {"video_url": "..."},
            "Бюджетные запросы": {
                "Свод по АБП/ГУ/ГККП": {"video_url": "...", "children": {...}}
            }
        }
    }
    """
    tree: Dict[str, Any] = {}

    for entry in entries:
        regime = entry["regime"]
        module = entry["module"]
        section = entry["section"]
        subsection = entry["subsection"]
        url = entry["video_url"]

        tree.setdefault(regime, {})

        if module:
            tree[regime].setdefault(module, {})
            if section:
                tree[regime][module].setdefault(section, {})
                if subsection:
                    tree[regime][module][section].setdefault("children", {})
                    tree[regime][module][section]["children"][subsection] = {"video_url": url}
                else:
                    tree[regime][module][section]["video_url"] = url
            else:
                tree[regime][module]["video_url"] = url
        else:
            tree[regime]["video_url"] = url

    return tree


def save_navigation_tree(entries: List[Dict[str, Any]], output_path: str) -> None:
    """Build and save navigation tree as JSON."""
    tree = build_navigation_tree(entries)
    out = Path(output_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        json.dump(tree, f, ensure_ascii=False, indent=2)
    logger.info("Navigation tree saved to %s", output_path)


def find_video_for_topic(
    entries: List[Dict[str, Any]],
    topic_section: str,
) -> Optional[str]:
    """Find the best matching video URL for a given topic/section name."""
    topic_lower = topic_section.lower().strip()
    for entry in entries:
        if topic_lower in entry.get("section", "").lower():
            return entry.get("video_url")
        if topic_lower in entry.get("subsection", "").lower():
            return entry.get("video_url")
        if topic_lower in entry.get("module", "").lower():
            return entry.get("video_url")
    return None
