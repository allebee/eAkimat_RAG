"""Module 3: Contextual Navigation — page_id → ChromaDB filter mapping."""

from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)

# Default mapping — will be overridden by data/context_mapping.json if it exists.
# Keys are page_id values sent by the frontend in X-Current-Context header.
_DEFAULT_MAPPING: Dict[str, Dict[str, Any]] = {
    # --- Бюджетное планирование ---
    "page_budget": {
        "label_ru": "Бюджетное планирование",
        "filter": {"regime": "budget_planning"},
    },
    "page_budget_requests": {
        "label_ru": "Бюджетные заявки",
        "filter": {"$and": [{"regime": "budget_planning"}, {"module": "budget_requests"}]},
    },
    "page_budget_svod": {
        "label_ru": "Свод по АБП/ГУ/ГККП",
        "filter": {"topic": "svod_abp_gu_gkkp"},
    },
    "page_budget_staffing": {
        "label_ru": "Штатное расписание",
        "filter": {"topic": "staffing"},
    },
    "page_budget_forms": {
        "label_ru": "Форма расчетов",
        "filter": {"topic": "calculation_forms"},
    },
    "page_budget_bip": {
        "label_ru": "БИП",
        "filter": {"topic": "bip"},
    },
    "page_budget_limits": {
        "label_ru": "Лимиты",
        "filter": {"topic": "limits"},
    },
    "page_budget_programs": {
        "label_ru": "Бюджетные программы",
        "filter": {"topic": "budget_programs"},
    },
    # --- Исполнение бюджета ---
    "page_execution": {
        "label_ru": "Исполнение бюджета",
        "filter": {"regime": "budget_execution"},
    },
    "page_execution_ipf": {
        "label_ru": "Индивидуальный план финансирования",
        "filter": {"topic": "ipf"},
    },
    "page_execution_changes": {
        "label_ru": "Заявки на внесение изменений",
        "filter": {"topic": "change_requests"},
    },
    "page_execution_monitoring": {
        "label_ru": "Мониторинг исполнения",
        "filter": {"topic": "monitoring"},
    },
    # --- Другие ---
    "page_media_monitoring": {
        "label_ru": "Медиамониторинг",
        "filter": {"regime": "media_monitoring"},
    },
    "page_personal": {
        "label_ru": "Личный кабинет",
        "filter": {"regime": "personal_account"},
    },
}

_mapping: Dict[str, Dict[str, Any]] = {}


def _load_mapping() -> Dict[str, Dict[str, Any]]:
    """Load context mapping from JSON file or use defaults."""
    global _mapping
    if _mapping:
        return _mapping

    config_path = Path("data/context_mapping.json")
    if config_path.exists():
        try:
            with open(config_path, "r", encoding="utf-8") as f:
                _mapping = json.load(f)
            logger.info("Loaded context mapping from %s (%d entries)", config_path, len(_mapping))
        except Exception as exc:
            logger.warning("Failed to load %s, using defaults: %s", config_path, exc)
            _mapping = _DEFAULT_MAPPING
    else:
        logger.info("No context_mapping.json found, using %d default entries", len(_DEFAULT_MAPPING))
        _mapping = _DEFAULT_MAPPING

    return _mapping


def get_chromadb_filter(page_id: str) -> Optional[Dict[str, Any]]:
    """Convert a page_id to a ChromaDB where-filter dict.

    Returns None if the page_id is not recognized.
    """
    mapping = _load_mapping()
    entry = mapping.get(page_id)
    if entry:
        return entry.get("filter")
    logger.warning("Unknown page_id: '%s', no filter applied", page_id)
    return None


def get_page_label(page_id: str, lang: str = "ru") -> str:
    """Get the human-readable label for a page_id."""
    mapping = _load_mapping()
    entry = mapping.get(page_id, {})
    label_key = f"label_{lang}"
    return entry.get(label_key, entry.get("label_ru", page_id))


def list_pages() -> Dict[str, str]:
    """Return all known page_id → label mappings."""
    mapping = _load_mapping()
    return {pid: entry.get("label_ru", pid) for pid, entry in mapping.items()}
