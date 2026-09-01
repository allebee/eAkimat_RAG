"""FastAPI routes for the eAkimat365 RAG service."""

from __future__ import annotations

import json
import logging
import re
import uuid
from pathlib import Path
from typing import Dict, List, Optional
from urllib.parse import quote

from fastapi import APIRouter, File, Header, HTTPException, UploadFile
from fastapi.concurrency import run_in_threadpool
from fastapi.responses import StreamingResponse

from app.api.schemas import (
    ChatRequest,
    ChatResponse,
    HealthResponse,
    IngestRequest,
    IngestResponse,
    MediaBlock,
    StatsResponse,
    TranscribeResponse,
)

logger = logging.getLogger(__name__)

router = APIRouter()

# In-memory conversation history (temporary — replace with Redis/DB later)
_conversations: Dict[str, list] = {}


def _encode_image_url(filename: str) -> str:
    """Build a fully encoded /images/ URL from a raw filename."""
    filename = filename.strip()
    if filename.startswith("/images/"):
        filename = filename[len("/images/"):]
    return f"/images/{quote(filename)}"


_IMAGE_DIR = Path("storage/images")
# Junk guard only — corrupt or blank files. Logos and glyphs are dropped at
# ingestion by page geometry (pdf_loader), which is far more accurate than a
# byte count, and every PDF chunk in the collection has been re-ingested through
# that filter. Size is a poor proxy for "is this a screenshot": the header logos
# this used to target are 3-4 KB, while genuine screenshots go down to 2.8 KB,
# so the old 15 KB threshold silently swallowed 13% of real screenshots.
_MIN_IMAGE_SIZE = 1_000

_SOURCE_LABEL_RE = re.compile(r"^[ \t]*\[ИСТОЧНИК:[^\]]*\][ \t]*\n?", re.MULTILINE)


def _strip_source_labels(text: str) -> str:
    """Remove any [ИСТОЧНИК: ...] provenance lines the model echoed back.

    The knowledge-base tool tags each chunk with its provenance so the agent
    knows whose interface wording it may trust. That tag is for the agent only —
    the prompt forbids copying it, and this strips it if the model does anyway.
    """
    return _SOURCE_LABEL_RE.sub("", text)


def _process_inline_images(text: str) -> str:
    """Convert [IMAGE: filename] markers to inline <img> HTML tags.

    Skips images below _MIN_IMAGE_SIZE — leftover logos/branding from chunks
    ingested before screenshot filtering moved into the PDF loader.
    """
    def _replace_image(match):
        raw = match.group(1).strip()
        # Get the bare filename (strip /images/ prefix if present)
        filename = raw
        if filename.startswith("/images/"):
            filename = filename[len("/images/"):]

        # Check if the image file exists and is large enough
        img_path = _IMAGE_DIR / filename
        if img_path.exists() and img_path.stat().st_size < _MIN_IMAGE_SIZE:
            # Too small — likely a logo/branding image, skip it
            return ""

        url = _encode_image_url(raw)
        return f'\n<img src="{url}" class="inline-screenshot" loading="lazy" alt="Скриншот инструкции"/>\n'

    return re.sub(r"\[IMAGE:\s*(.+?)\]", _replace_image, text)


def _extract_videos(text: str) -> tuple[str, List[MediaBlock]]:
    """Extract [VIDEO: url] markers and return clean text + video blocks."""
    videos: List[MediaBlock] = []

    for match in re.finditer(r"\[VIDEO:\s*(.+?)\]", text):
        url = match.group(1).strip()
        # Only include real URLs, not hallucinated ones
        if url.startswith("http") and "example.com" not in url:
            videos.append(MediaBlock(type="video", url=url))

    clean = re.sub(r"\[VIDEO:\s*.+?\]", "", text)
    clean = re.sub(r"\n{3,}", "\n\n", clean).strip()

    return clean, videos


@router.post("/chat", response_model=ChatResponse)
async def chat(
    request: ChatRequest,
    x_current_context: Optional[str] = Header(None),
) -> ChatResponse:
    """Main chat endpoint — processes user questions through the RAG agent."""
    from langchain_core.messages import AIMessage, HumanMessage

    from app.agent.graph import run_agent

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
        raw_response = await run_agent(
            message=request.message,
            context_page=x_current_context,
            language=request.language,
            chat_history=history[-10:],
        )

        # 1. Convert [IMAGE:] markers to inline <img> tags
        answer_with_images = _process_inline_images(_strip_source_labels(raw_response))

        # 2. Extract [VIDEO:] into separate media blocks (shown at bottom)
        answer_text, video_blocks = _extract_videos(answer_with_images)

        # Update conversation history (store raw response for LLM context)
        history.append(HumanMessage(content=request.message))
        history.append(AIMessage(content=raw_response))
        _conversations[conv_id] = history

        return ChatResponse(
            answer=answer_text,
            media=video_blocks,
            sources=[],
            conversation_id=conv_id,
        )

    except Exception as exc:
        logger.exception("Agent error: %s", exc)
        raise HTTPException(status_code=500, detail=f"Agent error: {str(exc)}")


# Human-facing labels for agent lifecycle stages (shown live in the UI while
# the user waits). Sent alongside the stage code so the frontend can display
# them directly.
_STATUS_LABELS = {
    "thinking": "Думаю над вопросом…",
    "searching": "Ищу инструкции и похожие обращения…",
    "generating": "Формирую ответ…",
}


@router.post("/chat/stream")
async def chat_stream(
    request: ChatRequest,
    x_current_context: Optional[str] = Header(None),
):
    """SSE streaming endpoint — emits live status events, then the answer."""
    from langchain_core.messages import AIMessage, HumanMessage

    from app.agent.graph import stream_agent

    conv_id = request.conversation_id or str(uuid.uuid4())
    history = _conversations.get(conv_id, [])

    async def event_stream():
        try:
            # 1. Drive the agent, forwarding lifecycle events as they happen.
            raw_response = ""
            async for ev in stream_agent(
                message=request.message,
                context_page=x_current_context,
                language=request.language,
                chat_history=history[-10:],
            ):
                if ev["kind"] == "status":
                    stage = ev["stage"]
                    data = json.dumps(
                        {
                            "type": "status",
                            "stage": stage,
                            "label": _STATUS_LABELS.get(stage, ""),
                        },
                        ensure_ascii=False,
                    )
                    yield f"data: {data}\n\n"
                elif ev["kind"] == "answer":
                    raw_response = ev["content"]

            # 2. Process images inline
            answer_with_images = _process_inline_images(_strip_source_labels(raw_response))
            answer_text, video_blocks = _extract_videos(answer_with_images)

            # Stream answer in smart chunks — keep <img> tags intact
            # Split on newlines so each line (including <img> tags) is sent whole
            lines = answer_text.split("\n")
            for i, line in enumerate(lines):
                chunk = line + ("\n" if i < len(lines) - 1 else "")
                if chunk:
                    data = json.dumps({"type": "text", "content": chunk}, ensure_ascii=False)
                    yield f"data: {data}\n\n"

            # Send video blocks if any
            for video in video_blocks:
                data = json.dumps(
                    {"type": "video", "url": video.url}, ensure_ascii=False
                )
                yield f"data: {data}\n\n"

            # Send done signal
            data = json.dumps({"type": "done", "conversation_id": conv_id})
            yield f"data: {data}\n\n"

            # Update history
            history.append(HumanMessage(content=request.message))
            history.append(AIMessage(content=raw_response))
            _conversations[conv_id] = history

        except Exception as exc:
            logger.exception("Stream error: %s", exc)
            data = json.dumps({"type": "error", "content": str(exc)})
            yield f"data: {data}\n\n"

    return StreamingResponse(
        event_stream(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",
        },
    )


# Singleton ASR engine — preloaded at startup (see lifespan in main.py) so the
# first /transcribe request is fast. Falls back to lazy load if preload was skipped.
_MAX_AUDIO_BYTES = 25 * 1024 * 1024  # 25 MB upload cap


def _get_asr_engine():
    from app.asr.engine import get_engine

    return get_engine()


@router.post("/transcribe", response_model=TranscribeResponse)
async def transcribe(audio: UploadFile = File(...)) -> TranscribeResponse:
    """Speech-to-text — принимает аудио (webm/ogg/wav/mp3/...) и возвращает текст.

    Использует двуязычную (RU+KK) Wav2Vec2-CTC модель. Инференс блокирующий
    и CPU-bound, поэтому выполняется в threadpool, чтобы не блокировать event loop.
    """
    data = await audio.read()
    if not data:
        raise HTTPException(status_code=400, detail="Пустой аудиофайл")
    if len(data) > _MAX_AUDIO_BYTES:
        raise HTTPException(status_code=413, detail="Аудиофайл слишком большой (макс. 25 МБ)")

    try:
        engine = await run_in_threadpool(_get_asr_engine)
        text = await run_in_threadpool(engine.transcribe_bytes, data)
    except Exception as exc:
        logger.exception("Transcription error: %s", exc)
        raise HTTPException(status_code=500, detail=f"Ошибка распознавания: {exc}")

    logger.info("Transcribed %d bytes -> '%s'", len(data), text[:100])
    return TranscribeResponse(text=text)


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
