"""FastAPI application entry point for the eAkimat365 RAG service."""

from __future__ import annotations

import logging
from contextlib import asynccontextmanager

import structlog
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings


def _configure_logging() -> None:
    """Set up structured logging."""
    logging.basicConfig(
        level=getattr(logging, settings.log_level.upper(), logging.INFO),
        format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
    )
    structlog.configure(
        processors=[
            structlog.stdlib.add_log_level,
            structlog.stdlib.add_logger_name,
            structlog.dev.ConsoleRenderer(),
        ],
        wrapper_class=structlog.stdlib.BoundLogger,
        logger_factory=structlog.stdlib.LoggerFactory(),
    )


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan — initialize services on startup."""
    _configure_logging()
    logger = logging.getLogger(__name__)

    logger.info("Starting eAkimat365 RAG Service")
    logger.info("LLM model: %s", settings.llm_model)
    logger.info("ChromaDB: %s", settings.chroma_path)

    # Pre-initialize ChromaDB
    try:
        from app.knowledge.chromadb_store import KnowledgeStore
        store = KnowledgeStore.get_instance()
        logger.info("ChromaDB ready: %d documents", store.count())
    except Exception as exc:
        logger.warning("ChromaDB initialization deferred: %s", exc)

    # Pre-load context mapping
    from app.knowledge.context_mapping import list_pages
    pages = list_pages()
    logger.info("Context mapping loaded: %d pages", len(pages))

    # Pre-load ASR model (warms GPU/CPU so the first /transcribe is fast)
    try:
        from app.asr.engine import get_engine
        engine = get_engine()
        logger.info("ASR model ready on device: %s", engine.device)
    except Exception as exc:
        logger.warning("ASR preload deferred: %s", exc)

    yield

    logger.info("Shutting down eAkimat365 RAG Service")


# Create app
app = FastAPI(
    title="eAkimat365 RAG Service",
    description="Agentic RAG system for Kazakhstan budget planning documentation",
    version="1.0.0",
    lifespan=lifespan,
)

# CORS
_cors_origins = settings.cors_origin_list
_allow_credentials = "*" not in _cors_origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=_cors_origins,
    allow_credentials=_allow_credentials,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
from pathlib import Path

from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from app.api.routes import router  # noqa: E402

app.include_router(router, prefix="/api")

# Serve extracted images
_storage_dir = Path("storage/images")
_storage_dir.mkdir(parents=True, exist_ok=True)
app.mount("/images", StaticFiles(directory=str(_storage_dir)), name="images")


@app.get("/")
async def root():
    """Serve the demo chat UI."""
    demo_path = Path("demo.html")
    if demo_path.exists():
        return FileResponse(str(demo_path), media_type="text/html")
    return {
        "service": "eAkimat365 RAG Service",
        "version": "1.0.0",
        "docs": "/docs",
    }
