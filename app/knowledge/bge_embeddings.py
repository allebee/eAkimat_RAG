"""Local BGE embeddings via sentence-transformers.

Drop-in replacement for ``langchain_openai.OpenAIEmbeddings`` — exposes the same
``embed_documents`` / ``embed_query`` interface so ``KnowledgeStore`` doesn't care
which provider is active.

We use ``BAAI/bge-m3`` by default: multilingual (RU + KK), 1024-dim. bge-m3 needs
no query-instruction prefix (unlike bge-large-en), so queries and documents are
encoded the same way. Vectors are L2-normalized so ChromaDB cosine distance is
consistent with the OpenAI path.
"""

from __future__ import annotations

import logging
from typing import List, Optional

logger = logging.getLogger(__name__)


def _resolve_device(pref: str) -> str:
    if pref and pref != "auto":
        return pref
    try:
        import torch

        return "cuda" if torch.cuda.is_available() else "cpu"
    except Exception:
        return "cpu"


class BGEEmbeddings:
    """Sentence-transformers BGE embedder with the LangChain embeddings interface."""

    _model = None  # class-level cache: load the ~2 GB model once per process

    def __init__(
        self,
        model_name: str = "BAAI/bge-m3",
        device: str = "auto",
        batch_size: int = 16,
    ) -> None:
        self.model_name = model_name
        self.device = _resolve_device(device)
        self.batch_size = batch_size
        self._ensure_model()

    def _ensure_model(self):
        if BGEEmbeddings._model is None:
            from sentence_transformers import SentenceTransformer

            logger.info(
                "Loading BGE embedding model '%s' on %s ...",
                self.model_name,
                self.device,
            )
            BGEEmbeddings._model = SentenceTransformer(
                self.model_name, device=self.device
            )
            logger.info("BGE embedding model loaded.")
        return BGEEmbeddings._model

    def _encode(self, texts: List[str]) -> List[List[float]]:
        model = self._ensure_model()
        vecs = model.encode(
            texts,
            batch_size=self.batch_size,
            normalize_embeddings=True,   # unit vectors -> cosine-ready
            convert_to_numpy=True,
            show_progress_bar=False,
        )
        return vecs.tolist()

    # LangChain-compatible interface -------------------------------------
    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        return self._encode(list(texts))

    def embed_query(self, text: str) -> List[float]:
        return self._encode([text])[0]
