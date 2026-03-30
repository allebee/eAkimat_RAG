"""Pydantic models for API request/response schemas."""

from __future__ import annotations

from typing import List, Literal, Optional

from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    """Incoming chat message from the frontend."""

    message: str = Field(..., min_length=1, max_length=5000, description="User's question")
    conversation_id: Optional[str] = Field(None, description="ID for multi-turn conversations")
    language: str = Field("ru", pattern="^(ru|kk)$", description="User's language: ru or kk")


class MediaBlock(BaseModel):
    """A media attachment in the response (image or video)."""

    type: Literal["image", "video"]
    url: str
    caption: Optional[str] = None


class ChatResponse(BaseModel):
    """Response from the agent."""

    answer: str = Field(..., description="Agent's text response")
    media: List[MediaBlock] = Field(default_factory=list, description="Attached images and videos")
    sources: List[str] = Field(default_factory=list, description="Source document references")
    conversation_id: str = Field(..., description="Conversation ID for continuity")


class HealthResponse(BaseModel):
    """Health check response."""

    status: str
    chromadb_docs: int
    postgres_connected: bool
    llm_model: str


class IngestRequest(BaseModel):
    """Request to trigger data ingestion."""

    pdf_dir: str = Field("./pdf", description="Path to PDF directory")
    faq_path: str = Field("./prod_data/FAQ.xlsx", description="Path to FAQ Excel file")
    instructions_path: str = Field(
        "./prod_data/instructions.xlsx", description="Path to instructions Excel file"
    )
    clear_existing: bool = Field(False, description="Clear existing ChromaDB data before ingesting")


class IngestResponse(BaseModel):
    """Response after ingestion."""

    status: str
    faq_count: int
    pdf_chunks_count: int
    unique_pdfs: int
    total_documents: int


class StatsResponse(BaseModel):
    """Collection statistics."""

    collection: str
    document_count: int
    persist_dir: str
