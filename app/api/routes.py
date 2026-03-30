"""FastAPI routes for the eAkimat365 RAG service."""

from __future__ import annotations

import logging
import re
import uuid
from pathlib import Path
from typing import Dict, List, Optional

from fastapi import APIRouter, Header, HTTPException

from app.api.schemas import (
    ChatRequest,
    ChatResponse,
    HealthResponse,
    IngestRequest,
    IngestResponse,
    MediaBlock,
    StatsResponse,
)

logger = logging.getLogger(__name__)

router = APIRouter()

# In-memory conversation history (temporary — replace with Redis/DB later)
_conversations: Dict[str, list] = {}


def _extract_media(text: str) -> tuple[str, List[MediaBlock]]:
    """Extract [IMAGE: ...] and [VIDEO: ...] markers from text.

    Returns clean text and list of media blocks.
    """
    media: List[MediaBlock] = []

    # Extract images
    for match in re.finditer(r"\[IMAGE:\s*(.+?)\]", text):
        media.append(MediaBlock(type="image", url=match.group(1).strip()))

    # Extract videos
    for match in re.finditer(r"\[VIDEO:\s*(.+?)\]", text):
        media.append(MediaBlock(type="video", url=match.group(1).strip()))

    # Clean markers from text
    clean_text = re.sub(r"\[IMAGE:\s*.+?\]", "", text)
    clean_text = re.sub(r"\[VIDEO:\s*.+?\]", "", clean_text)
    clean_text = re.sub(r"\n{3,}", "\n\n", clean_text).strip()

    return clean_text, media


@router.post("/chat", response_model=ChatResponse)
async def chat(
    request: ChatRequest,
    x_current_context: Optional[str] = Header(None),
) -> ChatResponse:
    """Main chat endpoint — processes user questions through the RAG agent.

    The frontend sends the user's current page context via X-Current-Context header.
    """
    from langchain_core.messages import AIMessage, HumanMessage

    from app.agent.graph import run_agent

    # Manage conversation history
    conv_id = request.conversation_id or str(uuid.uuid4())
    history = _conversations.get(conv_id, [])

    logger.info(
        "Chat request: conv=%s, context=%s, lang=%s, message='%s'",
        conv_id,
        x_current_context,
        request.language,
        request.message[:100],
    )

    try:
        # Run the agent
        raw_response = await run_agent(
            message=request.message,
            context_page=x_current_context,
            language=request.language,
            chat_history=history[-10:],  # Keep last 10 messages for context
        )

        # Extract media from response
        answer_text, media_blocks = _extract_media(raw_response)

        # Update conversation history
        history.append(HumanMessage(content=request.message))
        history.append(AIMessage(content=raw_response))
        _conversations[conv_id] = history

        return ChatResponse(
            answer=answer_text,
            media=media_blocks,
            sources=[],
            conversation_id=conv_id,
        )

    except Exception as exc:
        logger.exception("Agent error: %s", exc)
        raise HTTPException(status_code=500, detail=f"Agent error: {str(exc)}")


@router.get("/health", response_model=HealthResponse)
async def health() -> HealthResponse:
    """Health check — verifies ChromaDB and reports status."""
    from app.config import settings

    try:
        from app.knowledge.chromadb_store import KnowledgeStore
        store = KnowledgeStore.get_instance()
        doc_count = store.count()
    except Exception:
        doc_count = -1

    pg_connected = False
    if settings.postgres_dsn and settings.postgres_dsn != "postgresql://readonly_user:password@localhost:5432/eakimat365":
        # TODO: actual PG health check
        pg_connected = False

    return HealthResponse(
        status="ok" if doc_count >= 0 else "degraded",
        chromadb_docs=doc_count,
        postgres_connected=pg_connected,
        llm_model=settings.llm_model,
    )


@router.post("/ingest", response_model=IngestResponse)
async def ingest(request: IngestRequest) -> IngestResponse:
    """Trigger data ingestion — loads FAQ and PDFs into ChromaDB."""
    from app.ingestion.deduplicator import deduplicate_pdfs
    from app.ingestion.faq_loader import load_faq
    from app.ingestion.pdf_loader import PDFLoader
    from app.knowledge.chromadb_store import KnowledgeStore

    store = KnowledgeStore.get_instance()

    if request.clear_existing:
        store.clear()
        logger.info("Cleared existing ChromaDB data")

    # 1. Load FAQ
    faq_docs = load_faq(request.faq_path)
    if faq_docs:
        store.add_documents(
            texts=[d["content"] for d in faq_docs],
            metadatas=[d["metadata"] for d in faq_docs],
            ids=[d["id"] for d in faq_docs],
        )
    logger.info("Ingested %d FAQ documents", len(faq_docs))

    # 2. Deduplicate and load PDFs
    pdf_dir = Path(request.pdf_dir)
    unique_pdfs = deduplicate_pdfs(pdf_dir) if pdf_dir.exists() else []

    loader = PDFLoader()
    total_chunks = 0
    for pdf_info in unique_pdfs:
        chunks = loader.load_pdf(pdf_info["path"], title=pdf_info["title"])
        if chunks:
            store.add_documents(
                texts=[c["content"] for c in chunks],
                metadatas=[c["metadata"] for c in chunks],
                ids=[c["id"] for c in chunks],
            )
            total_chunks += len(chunks)

    logger.info("Ingested %d PDF chunks from %d unique PDFs", total_chunks, len(unique_pdfs))

    return IngestResponse(
        status="completed",
        faq_count=len(faq_docs),
        pdf_chunks_count=total_chunks,
        unique_pdfs=len(unique_pdfs),
        total_documents=store.count(),
    )


@router.get("/stats", response_model=StatsResponse)
async def stats() -> StatsResponse:
    """Get collection statistics."""
    from app.knowledge.chromadb_store import KnowledgeStore

    store = KnowledgeStore.get_instance()
    s = store.stats()
    return StatsResponse(**s)
