"""Module 1 Tool: Knowledge base search via ChromaDB.

Retrieval is *source-aware*. The collection is dominated by call-center Q&A
(~86% of docs), so a plain cosine top-k almost never surfaces the official PDF
instructions or the video screenshots — those carry the [IMAGE:] markers and the
canonical steps. We therefore query two buckets separately and merge them:

  • INSTRUCTIONAL (pdf_instruction + video) — canonical steps + screenshots
  • CASES        (call_center + support_call) — real, practical Q&A from support

Each bucket is filtered by relevance, then merged under a quota so an answer can
contain BOTH the authoritative instruction (with a screenshot) AND a real case.
"""

from __future__ import annotations

import asyncio
import logging
from typing import Any, Dict, List, Optional

from langchain_core.tools import tool

logger = logging.getLogger(__name__)

# Distance thresholds for ChromaDB cosine similarity
GOOD_MATCH_THRESHOLD = 0.3    # Below this = confident match
WEAK_MATCH_THRESHOLD = 0.6    # Above this = low quality, drop

# Source buckets
INSTRUCTIONAL = ["pdf_instruction", "video"]
CASES = ["call_center", "support_call"]

# Retrieval budget
BUCKET_K = 6          # candidates pulled per bucket
MAX_INSTRUCTIONAL = 3  # canonical chunks kept
MAX_CASES = 3          # case chunks kept
MAX_TOTAL = 6          # total chunks handed to the LLM


def _merge_where(
    base: Optional[Dict[str, Any]], source_types: List[str]
) -> Dict[str, Any]:
    """Combine an optional page-context filter with a source_type restriction."""
    src = {"source_type": {"$in": source_types}}
    if base:
        return {"$and": [base, src]}
    return src


def _has_image(doc: Dict[str, Any]) -> bool:
    return "[IMAGE:" in (doc.get("content") or "")


def _select(
    instructional: List[Dict[str, Any]], cases: List[Dict[str, Any]]
) -> List[Dict[str, Any]]:
    """Merge the two buckets under quotas, guaranteeing a screenshot when one exists.

    Both inputs are pre-sorted by distance (best first) and pre-filtered by the
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
        leftovers.sort(key=lambda d: d["distance"])
        chosen.extend(leftovers[: MAX_TOTAL - len(chosen)])

    # Order the final set best-first for the LLM.
    chosen.sort(key=lambda d: d["distance"])
    return chosen[:MAX_TOTAL]


@tool
async def search_knowledge_base(
    query: str,
    context_page: Optional[str] = None,
) -> str:
    """Search the eAkimat365 knowledge base for instructions, FAQ, and how-to guides.

    Use this tool when the user asks about how to use the system, where to find
    buttons, how to fill forms, or any procedural question.

    DO NOT use this tool for questions about specific numbers (budget, plan, fact).

    The returned text contains [IMAGE: filename.jpeg] markers at the exact
    positions where screenshots should appear. You MUST pass these markers
    through unchanged in your response so the frontend can render them.

    Args:
        query: The user's question in Russian or Kazakh.
        context_page: Optional page_id from the frontend context (e.g. 'page_budget_staffing').
    """
    from app.knowledge.chromadb_store import KnowledgeStore
    from app.knowledge.context_mapping import get_chromadb_filter

    store = KnowledgeStore.get_instance()

    page_filter = get_chromadb_filter(context_page) if context_page else None

    # Two targeted searches so the majority class (call-center) cannot crowd out
    # the canonical instructions + screenshots. Run both buckets concurrently in
    # threads so the (sync) embedding + Chroma work does not block the event loop
    # and the two network embeds overlap.
    instructional, cases = await asyncio.gather(
        asyncio.to_thread(
            store.search, query, BUCKET_K, _merge_where(page_filter, INSTRUCTIONAL)
        ),
        asyncio.to_thread(
            store.search, query, BUCKET_K, _merge_where(page_filter, CASES)
        ),
    )

    # Drop low-quality matches per bucket.
    instructional = [d for d in instructional if d["distance"] < WEAK_MATCH_THRESHOLD]
    cases = [d for d in cases if d["distance"] < WEAK_MATCH_THRESHOLD]

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
        "KB search: %d instructional + %d cases -> %d chunks (sources: %s)",
        len(instructional),
        len(cases),
        len(selected),
        [d["metadata"].get("source_type", "?") for d in selected],
    )

    response = "\n\n---\n\n".join(d["content"] for d in selected)

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
