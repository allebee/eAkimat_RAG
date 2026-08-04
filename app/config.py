"""Application configuration loaded from environment variables."""

from __future__ import annotations

import json
from pathlib import Path
from typing import List

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Central configuration for the eAkimat365 RAG service."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # --- LLM provider switch: "grok" or "deepseek" ---
    llm_provider: str = "grok"

    # --- LLM (xAI Grok) ---
    grok_api_key: str = ""
    grok_model: str = "grok-4-fast-non-reasoning"
    grok_base_url: str = "https://api.x.ai/v1"

    # --- LLM (DeepSeek — also OpenAI-compatible) ---
    deepseek_api_key: str = ""
    deepseek_model: str = "deepseek-chat"
    deepseek_base_url: str = "https://api.deepseek.com"

    # --- Embeddings ---
    # Provider switch: "openai" (hosted API) or "bge" (local sentence-transformers).
    # NOTE: switching provider changes the vector DIMENSION, so the whole ChromaDB
    # collection must be re-ingested from scratch (--clear). Query- and index-time
    # embeddings must use the same model.
    embedding_provider: str = "openai"

    # OpenAI hosted embeddings
    openai_api_key: str = ""
    embedding_model: str = "text-embedding-3-small"

    # BGE local embeddings (BAAI/bge-m3 — multilingual RU+KK, 1024-dim)
    bge_model: str = "BAAI/bge-m3"
    bge_device: str = "auto"   # "auto" -> cuda if available else cpu; or "cuda"/"cpu"
    bge_batch_size: int = 16

    @property
    def llm_model(self) -> str:
        """Active LLM model name."""
        if self.llm_provider == "deepseek":
            return self.deepseek_model
        return self.grok_model

    @property
    def llm_api_key(self) -> str:
        """API key for the active LLM provider."""
        if self.llm_provider == "deepseek":
            return self.deepseek_api_key
        return self.grok_api_key

    @property
    def llm_base_url(self) -> str:
        """Base URL for the active LLM provider."""
        if self.llm_provider == "deepseek":
            return self.deepseek_base_url
        return self.grok_base_url

    # --- ChromaDB ---
    chroma_persist_dir: str = "./chroma_data"
    chroma_collection: str = "eakimat365_knowledge"

    # --- PostgreSQL (Module 2) ---
    postgres_dsn: str = ""

    # --- LangChain ---
    langchain_tracing_v2: bool = False
    langchain_api_key: str = ""
    langchain_project: str = "eakimat365-rag"

    # --- App ---
    log_level: str = "INFO"
    cors_origins: str = '["http://localhost:3000"]'
    storage_dir: str = "./storage"

    # --- Derived ---
    @property
    def cors_origin_list(self) -> List[str]:
        """Parse CORS origins from JSON string."""
        try:
            return json.loads(self.cors_origins)
        except (json.JSONDecodeError, TypeError):
            return ["http://localhost:3000"]

    @property
    def storage_path(self) -> Path:
        return Path(self.storage_dir)

    @property
    def images_path(self) -> Path:
        return self.storage_path / "images"

    @property
    def chroma_path(self) -> Path:
        return Path(self.chroma_persist_dir)


# Singleton
settings = Settings()
