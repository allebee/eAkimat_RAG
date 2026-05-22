"""Module 1 Tool: Knowledge base search via ChromaDB."""

from __future__ import annotations

import logging
from typing import Optional

from langchain_core.tools import tool

logger = logging.getLogger(__name__)

# Distance thresholds for ChromaDB cosine similarity
GOOD_MATCH_THRESHOLD = 0.3    # Below this = confident match
WEAK_MATCH_THRESHOLD = 0.6    # Above this = low quality


@tool
def search_knowledge_base(
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

    store = KnowledgeStore.get_instance()

    # Search with context filter first
    results = store.search_with_context(query, page_context=context_page, k=8)

    if not results:
        return "В базе знаний не найден ответ на данный вопрос. Рекомендуется обратиться в техническую поддержку."

    # Evaluate match quality
    best_distance = results[0]["distance"]
    response_parts: list[str] = []

    # Collect relevant results (top 5)
    for doc in results[:5]:
        if doc["distance"] < WEAK_MATCH_THRESHOLD:
            response_parts.append(doc["content"])

    if not response_parts:
        response_parts.append(results[0]["content"])

    response = "\n\n---\n\n".join(response_parts)

    # Add video link ONLY if a real video URL exists in the metadata
    # and only if the match quality is weak (user might benefit from video)
    seen_video = False
    for doc in results[:3]:
        meta = doc.get("metadata", {})
        vid = meta.get("video_url", "")
        # Only include real video URLs, not empty strings or example URLs
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
