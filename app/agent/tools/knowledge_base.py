"""Module 1 Tool: Knowledge base search via ChromaDB.

Retrieval is *source-aware*. The collection is dominated by call-center Q&A
(~86% of docs), so a plain cosine top-k almost never surfaces the official PDF
instructions or the video screenshots — those carry the [IMAGE:] markers and the
canonical steps. We therefore query two buckets separately and merge them:

  • INSTRUCTIONAL (pdf_instruction + video) — canonical steps + screenshots
  • CASES        (call_center + support_call) — real, practical Q&A from support

Each bucket is filtered by relevance, then merged under a quota so an answer can
contain BOTH the authoritative instruction (with a screenshot) AND a real case.

Retrieval is also *module-aware*. Modules share almost all of their vocabulary —
"Заявки ГУ" and "Формы расчётов" both talk about спецификации 311/420, отправка
на согласование and остатки — so cosine similarity alone routinely answered about
the wrong module. When a question names a module we pull extra candidates from it
and re-score everything, which reorders near-ties without excluding anything.
"""

from __future__ import annotations

import asyncio
import logging
from typing import Any, Dict, List, Optional

from langchain_core.tools import tool

from app.knowledge.topics import detect_topic, score_delta

logger = logging.getLogger(__name__)

# Distance thresholds for ChromaDB cosine similarity
GOOD_MATCH_THRESHOLD = 0.3    # Below this = confident match
WEAK_MATCH_THRESHOLD = 0.6    # Above this = low quality, drop

# Source buckets
INSTRUCTIONAL = ["pdf_instruction", "video"]
CASES = ["call_center", "support_call"]

# Retrieval budget
BUCKET_K = 6          # candidates pulled per bucket
TOPIC_K = 4           # extra candidates from the module the question names
MAX_INSTRUCTIONAL = 3  # canonical chunks kept
MAX_CASES = 3          # case chunks kept
MAX_TOTAL = 6          # total chunks handed to the LLM

# Shown to the LLM above each chunk. The agent may only take interface wording
# (button, field and status names) from an official source — support cases are
# paraphrased by operators and introduce terms that do not exist in eAkimat365.
SOURCE_LABELS = {
    "pdf_instruction": "официальная инструкция",
    "video": "видео-инструкция",
    "call_center": "обращение в поддержку",
    "support_call": "обращение в поддержку",
}
DEFAULT_SOURCE_LABEL = "база знаний"


def _merge_where(
    base: Optional[Dict[str, Any]], source_types: List[str]
) -> Dict[str, Any]:
    """Combine an optional page-context filter with a source_type restriction."""
    src = {"source_type": {"$in": source_types}}
    if base:
        return {"$and": [base, src]}
    return src


def _topic_where(base: Optional[Dict[str, Any]], topic: str) -> Dict[str, Any]:
    """Filter for official instructions belonging to one module.

    Restricted to pdf_instruction: it is the only source whose `topic` uses the
    controlled vocabulary. Video topics are free-form LLM labels and call-center
    topics are coarse, so neither can be filtered this way.
    """
    clauses: List[Dict[str, Any]] = [
        {"source_type": "pdf_instruction"},
        {"topic": topic},
    ]
    if base:
        clauses.insert(0, base)
    return {"$and": clauses}


def _dedupe(docs: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Drop repeat hits, keeping the first (highest-priority) copy of each."""
    seen: set = set()
    unique: List[Dict[str, Any]] = []
    for doc in docs:
        if doc["id"] in seen:
            continue
        seen.add(doc["id"])
        unique.append(doc)
    return unique


def _has_image(doc: Dict[str, Any]) -> bool:
    return "[IMAGE:" in (doc.get("content") or "")


def _select(
    instructional: List[Dict[str, Any]], cases: List[Dict[str, Any]]
) -> List[Dict[str, Any]]:
    """Merge the two buckets under quotas, guaranteeing a screenshot when one exists.

    Both inputs are pre-sorted by score (best first) and pre-filtered by the
    weak-match threshold.
    """
    chosen: List[Dict[str, Any]] = []

    # Keep the top instructional chunks, but make sure at least one screenshot-
    # bearing chunk is present if a relevant one exists — that is the whole point
    # of keeping PDFs/video in the mix.
    inst_pick = instructional[:MAX_INSTRUCTIONAL]
    if inst_pick and not any(_has_image(d) for d in inst_pick):
        for d in instructional[MAX_INSTRUCTIONAL:]:
            if _has_image(d):
                inst_pick[-1] = d  # swap the weakest non-image chunk for a screenshot
                break
    chosen.extend(inst_pick)

    # Add the top case chunks.
    chosen.extend(cases[:MAX_CASES])

    # Backfill from whichever bucket has more, if we're under budget.
    if len(chosen) < MAX_TOTAL:
        leftovers = instructional[len(inst_pick):] + cases[MAX_CASES:]
        leftovers.sort(key=lambda d: d["score"])
        chosen.extend(leftovers[: MAX_TOTAL - len(chosen)])

    # Order the final set best-first for the LLM.
    chosen.sort(key=lambda d: d["score"])
    return chosen[:MAX_TOTAL]


@tool
async def search_knowledge_base(
    query: str,
    context_page: Optional[str] = None,
    module: Optional[str] = None,
) -> str:
    """Search the eAkimat365 knowledge base for instructions, FAQ, and how-to guides.

    Use this tool when the user asks about how to use the system, where to find
    buttons, how to fill forms, or any procedural question.

    DO NOT use this tool for questions about specific numbers (budget, plan, fact).

    The returned text contains [IMAGE: filename.jpeg] markers at the exact
    positions where screenshots should appear. You MUST pass these markers
    through unchanged in your response so the frontend can render them.

    Each chunk is prefixed with [ИСТОЧНИК: ...]. Never copy that line into your
    answer — it tells you how far to trust the chunk's wording.

    Args:
        query: The user's question in Russian or Kazakh.
        context_page: Optional page_id from the frontend context (e.g. 'page_budget_staffing').
        module: The eAkimat365 mode/section the user is asking about, exactly as
            they named it ("Заявки ГУ", "Формы расчётов", "Справки", "Штатное
            расписание", ...). Pass it whenever the user has named a module
            ANYWHERE in the conversation, including earlier turns — modules share
            wording, so without this the search can answer about the wrong one.
    """
    from app.knowledge.chromadb_store import KnowledgeStore
    from app.knowledge.context_mapping import get_chromadb_filter

    store = KnowledgeStore.get_instance()

    page_filter = get_chromadb_filter(context_page) if context_page else None
    topic = detect_topic(module or "", query)

    # Targeted searches so the majority class (call-center) cannot crowd out the
    # canonical instructions + screenshots, plus — when the question names a
    # module — a third search that guarantees that module's official instruction
    # is among the candidates. Run them concurrently in threads so the (sync)
    # embedding + Chroma work does not block the event loop and the embeds overlap.
    searches = [
        asyncio.to_thread(
            store.search, query, BUCKET_K, _merge_where(page_filter, INSTRUCTIONAL)
        ),
        asyncio.to_thread(
            store.search, query, BUCKET_K, _merge_where(page_filter, CASES)
        ),
    ]
    if topic:
        searches.append(
            asyncio.to_thread(store.search, query, TOPIC_K, _topic_where(page_filter, topic))
        )

    results = await asyncio.gather(*searches)
    instructional, cases = results[0], results[1]
    if topic:
        # Module-specific hits lead, so they win ties during de-duplication.
        instructional = _dedupe(results[2] + instructional)

    # Drop low-quality matches per bucket, on raw distance — the module bonus
    # below reorders candidates but must not rescue a genuinely poor match.
    instructional = [d for d in instructional if d["distance"] < WEAK_MATCH_THRESHOLD]
    cases = [d for d in cases if d["distance"] < WEAK_MATCH_THRESHOLD]

    for doc in (*instructional, *cases):
        doc["score"] = doc["distance"] + score_delta(
            topic, doc.get("metadata", {}), doc.get("content", "")
        )
    instructional.sort(key=lambda d: d["score"])
    cases.sort(key=lambda d: d["score"])

    selected = _select(instructional, cases)

    # Fallback: nothing passed the threshold in either bucket — take the single
    # best match overall (page filter still respected).
    if not selected:
        loose = await asyncio.to_thread(store.search, query, 8, page_filter)
        if not loose:
            return (
                "В базе знаний не найден ответ на данный вопрос. "
                "Рекомендуется обратиться в техническую поддержку."
            )
        selected = loose[:1]

    logger.info(
        "KB search: %d instructional + %d cases -> %d chunks (topic=%s, sources: %s)",
        len(instructional),
        len(cases),
        len(selected),
        topic or "-",
        [d["metadata"].get("source_type", "?") for d in selected],
    )

    # Label every chunk with its provenance so the agent knows which wording is
    # authoritative: interface terms may only come from an official instruction.
    response = "\n\n---\n\n".join(
        f"[ИСТОЧНИК: {SOURCE_LABELS.get(d['metadata'].get('source_type', ''), DEFAULT_SOURCE_LABEL)}]"
        f"\n{d['content']}"
        for d in selected
    )

    # Offer a video link only when the best match is weak (text may be unclear).
    best_distance = selected[0]["distance"]
    seen_video = False
    for doc in selected:
        meta = doc.get("metadata", {})
        vid = meta.get("video_url", "")
        if (
            vid
            and not seen_video
            and vid.startswith("http")
            and "example.com" not in vid
            and best_distance > GOOD_MATCH_THRESHOLD
        ):
            response += (
                f"\n\nЕсли текстовая инструкция недостаточно понятна, "
                f"посмотрите видео-инструкцию:\n[VIDEO: {vid}]"
            )
            seen_video = True

    return response
