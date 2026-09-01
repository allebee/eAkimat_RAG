"""Topic detection for retrieval — maps free text to the `topic` metadata key.

Retrieval used to be pure cosine similarity, which made the agent answer about a
different eAkimat365 module than the one the user asked about: "Заявки ГУ" and
"Формы расчётов" share nearly all of their vocabulary (спецификации 311/420,
отправка на согласование, остатки по спецификации), so the nearest chunks
routinely came from the wrong module. Here we recognise the module a question
names, so retrieval can prefer chunks from that module.

Three different `topic` vocabularies coexist in the collection:
  • pdf_instruction — the controlled keys below (pdf_loader.normalize_topic)
  • video           — free-form LLM labels ("Управление Бюджетными Заявками", 988 of them)
  • call_center     — a coarse 6-value map, frequently empty
Only the first can be filtered on, so a detected topic is used to *add* targeted
candidates and to re-score, never to exclude — otherwise video and call-center
chunks (which cannot match a controlled key) would all be filtered away.
"""

from __future__ import annotations

import re
from typing import Any, Dict, Optional, Tuple

# Phrases a user may type → the controlled `topic` key stored on PDF chunks.
# Declensions are listed explicitly: the corpus is Russian and we match on
# substrings, so "заявке ГУ" must be spelled out to be found. Text is normalised
# (lowercased, ё→е, whitespace collapsed) before matching, and the LONGEST
# matching alias wins so "лимиты расход" beats the bare "лимиты".
TOPIC_ALIASES: Dict[str, Tuple[str, ...]] = {
    "gu_requests": (
        "заявки гу", "заявка гу", "заявку гу", "заявке гу",
        "заявок гу", "заявках гу", "заявкам гу", "заявками гу",
    ),
    "calculation_forms": (
        "форма расчет", "формы расчет", "форму расчет", "форме расчет",
        "форм расчет", "формах расчет", "формам расчет", "формами расчет",
        "расчетная форма", "расчетной формы", "расчетных форм",
    ),
    "references": (
        "справка", "справки", "справку", "справке", "справок",
        "справках", "справкам", "справками", "внутренняя справка",
        "внутренней справке", "внутренней справки",
    ),
    "svod_abp_gu_gkkp": (
        "свод по абп", "свод по гу", "свод по гккп", "свода по абп",
        "своде по абп", "сводом по абп", "сводная заявка", "сводной заявки",
    ),
    "staffing": (
        "штатное расписание", "штатного расписания", "штатном расписании",
        "штатному расписанию", "штатным расписанием", "штатка", "штатки",
        "штатке", "штатку",
    ),
    "bip": (
        "бип", "бюджетные инвестиционные проекты",
        "бюджетных инвестиционных проектов", "инвестиционный проект",
        "инвестиционного проекта", "инвестиционные проекты",
    ),
    "limits": ("лимиты", "лимитов", "лимитам", "лимитах", "лимит"),
    "limits_income": ("лимиты доход", "лимит доход", "лимитов доход"),
    "limits_expenses": ("лимиты расход", "лимит расход", "лимитов расход"),
    "limits_distribution": (
        "нормативы распределения", "норматив распределения",
        "нормативов распределения",
    ),
    "ipf": (
        "ипф", "индивидуальный план финансирования",
        "индивидуального плана финансирования",
        "индивидуальном плане финансирования",
        "спф", "сводный план финансирования", "сводного плана финансирования",
    ),
    "correction_expenses": (
        "корректировка расход", "корректировки расход", "корректировку расход",
        "корректировке расход", "корректировка расходной",
        "корректировки расходной", "корректировку расходной",
    ),
    "correction_income": (
        "корректировка доход", "корректировки доход", "корректировку доход",
        "корректировке доход", "корректировка доходной",
        "корректировки доходной", "корректировку доходной",
    ),
    "refinement_expenses": (
        "уточнение расход", "уточнения расход", "уточнении расход",
        "уточненный план расход", "уточнение расходной",
    ),
    "refinement_income": (
        "уточнение доход", "уточнения доход", "уточнении доход",
        "уточненный план доход", "уточнение доходной",
    ),
    "expense_formation": (
        "формирование расходной части", "формирования расходной части",
        "формировании расходной части", "расходная часть бюджета",
        "расходной части бюджета",
    ),
    "income_formation": (
        "формирование доходной части", "формирования доходной части",
        "формировании доходной части", "доходная часть бюджета",
        "доходной части бюджета",
    ),
    "consolidated_reports": (
        "сводные отчеты", "сводный отчет", "сводных отчетов",
        "сводного отчета", "сводном отчете",
    ),
    "media_monitoring": ("медиамониторинг", "медиа мониторинг", "медиамониторинга"),
    "registration_access": (
        "права доступа", "прав доступа", "регистрационные данные",
        "регистрационных данных", "регистрационными данными",
    ),
    "budget_programs": (
        "бюджетная программа", "бюджетные программы", "бюджетных программ",
        "бюджетной программы", "бюджетную программу", "бюджетной программе",
    ),
    "target_indicators": (
        "целевые индикаторы", "целевых индикаторов", "целевыми индикаторами",
        "взаимоувязка",
    ),
    "development_expenses": ("расходы развития", "расходов развития"),
    "project_evaluation": ("оценка проектов", "оценки проектов", "оценку проектов"),
    "signatories": ("подписанты", "подписантов", "подписантами"),
    "forma_gu": ("форма гу", "формы гу", "форме гу", "форму гу"),
    "snp_needs": ("потребности снп", "снп"),
    "sep": ("сэп",),
    "sem": ("сэм",),
}

# Topics we can recognise from a question. A chunk tagged with one of these but a
# *different* one than the question names is actively about another module, so it
# earns a penalty. Free-form video topics are not in this set and are never
# penalised — they simply cannot be judged this way.
KNOWN_TOPICS = frozenset(TOPIC_ALIASES)

# Score adjustments, in ChromaDB cosine-distance units (lower = better match).
# Sized against the retrieval thresholds in knowledge_base.py (good < 0.3,
# weak > 0.6): enough to reorder near-ties, not enough to drag in a poor match.
TOPIC_MATCH_BONUS = 0.15      # chunk's own topic == the topic the question names
ALIAS_HIT_BONUS = 0.08        # chunk text mentions the module by name
TOPIC_MISMATCH_PENALTY = 0.10  # chunk is tagged as a different known module


def _normalize(text: str) -> str:
    """Lowercase, fold ё→е, and collapse whitespace for substring matching."""
    return re.sub(r"\s+", " ", text.lower().replace("ё", "е")).strip()


def detect_topic(*texts: str) -> Optional[str]:
    """Return the controlled topic key named in the given texts, if any.

    Texts are checked in order and the first one that names a module wins, so a
    caller can pass an explicit module hint ahead of the raw question. Within a
    single text the longest matching alias wins, so a specific module beats the
    generic one it contains.
    """
    for raw in texts:
        if not raw:
            continue
        norm = _normalize(raw)
        best: Optional[str] = None
        best_len = 0
        for topic, aliases in TOPIC_ALIASES.items():
            for alias in aliases:
                if len(alias) > best_len and alias in norm:
                    best, best_len = topic, len(alias)
        if best:
            return best
    return None


def score_delta(
    detected_topic: Optional[str],
    metadata: Dict[str, Any],
    content: str,
) -> float:
    """Distance adjustment for one candidate chunk (negative = promote).

    Works across all three `topic` vocabularies: chunks carrying the controlled
    key are matched on metadata, everything else is judged by whether the module
    is named in the chunk text itself.
    """
    if not detected_topic:
        return 0.0

    doc_topic = (metadata or {}).get("topic", "") or ""
    if doc_topic == detected_topic:
        return -TOPIC_MATCH_BONUS

    delta = 0.0
    if doc_topic in KNOWN_TOPICS:
        delta += TOPIC_MISMATCH_PENALTY

    norm_content = _normalize(content or "")
    if any(alias in norm_content for alias in TOPIC_ALIASES[detected_topic]):
        delta -= ALIAS_HIT_BONUS

    return delta
