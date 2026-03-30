"""ChromaDB vector store wrapper for the eAkimat365 knowledge base."""

from __future__ import annotations

import logging
from typing import Any, Dict, List, Optional

import chromadb
from chromadb.config import Settings as ChromaSettings
from langchain_openai import OpenAIEmbeddings

from app.config import settings

logger = logging.getLogger(__name__)


class KnowledgeStore:
    """Singleton wrapper around ChromaDB for knowledge base operations."""

    _instance: Optional["KnowledgeStore"] = None

    def __init__(self) -> None:
        settings.chroma_path.mkdir(parents=True, exist_ok=True)

        self._client = chromadb.PersistentClient(
            path=str(settings.chroma_path),
            settings=ChromaSettings(anonymized_telemetry=False),
        )
        self._collection = self._client.get_or_create_collection(
            name=settings.chroma_collection,
            metadata={"hnsw:space": "cosine"},
        )
        self._embeddings = OpenAIEmbeddings(
            model=settings.embedding_model,
            openai_api_key=settings.openai_api_key,
        )
        logger.info(
            "ChromaDB initialized: collection=%s, docs=%d",
            settings.chroma_collection,
            self._collection.count(),
        )

    @classmethod
    def get_instance(cls) -> "KnowledgeStore":
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    # ------------------------------------------------------------------
    # Write
    # ------------------------------------------------------------------

    def add_documents(
        self,
        texts: List[str],
        metadatas: List[Dict[str, Any]],
        ids: List[str],
    ) -> None:
        """Add documents with embeddings to the collection."""
        # Sanitize metadata: ChromaDB does not accept None values
        clean_metadatas = []
        for meta in metadatas:
            clean = {}
            for k, v in meta.items():
                if v is None:
                    clean[k] = ""
                else:
                    clean[k] = v
            clean_metadatas.append(clean)

        embeddings = self._embeddings.embed_documents(texts)
        self._collection.upsert(
            ids=ids,
            documents=texts,
            embeddings=embeddings,
            metadatas=clean_metadatas,
        )
        logger.info("Upserted %d documents", len(ids))

    def clear(self) -> None:
        """Delete all documents from the collection."""
        self._client.delete_collection(settings.chroma_collection)
        self._collection = self._client.get_or_create_collection(
            name=settings.chroma_collection,
            metadata={"hnsw:space": "cosine"},
        )
        logger.info("Collection cleared")

    # ------------------------------------------------------------------
    # Read
    # ------------------------------------------------------------------

    def search(
        self,
        query: str,
        k: int = 5,
        where_filter: Optional[Dict[str, Any]] = None,
    ) -> List[Dict[str, Any]]:
        """Semantic search with optional metadata filtering.

        Returns list of dicts with keys: id, content, metadata, distance.
        """
        query_embedding = self._embeddings.embed_query(query)

        kwargs: Dict[str, Any] = {
            "query_embeddings": [query_embedding],
            "n_results": k,
            "include": ["documents", "metadatas", "distances"],
        }
        if where_filter:
            kwargs["where"] = where_filter

        try:
            results = self._collection.query(**kwargs)
        except Exception as exc:
            logger.warning("ChromaDB query failed (filter=%s): %s", where_filter, exc)
            # Retry without filter as fallback
            kwargs.pop("where", None)
            results = self._collection.query(**kwargs)

        docs: List[Dict[str, Any]] = []
        if results and results["ids"] and results["ids"][0]:
            for i, doc_id in enumerate(results["ids"][0]):
                docs.append(
                    {
                        "id": doc_id,
                        "content": results["documents"][0][i],
                        "metadata": results["metadatas"][0][i],
                        "distance": results["distances"][0][i],
                    }
                )
        return docs

    def search_with_context(
        self,
        query: str,
        page_context: Optional[str] = None,
        k: int = 5,
    ) -> List[Dict[str, Any]]:
        """Search with automatic context-based filtering (Module 3).

        If page_context is provided, builds a metadata filter from the
        context mapping configuration.
        """
        from app.knowledge.context_mapping import get_chromadb_filter

        where_filter = None
        if page_context:
            where_filter = get_chromadb_filter(page_context)
            logger.info("Context filter for '%s': %s", page_context, where_filter)

        return self.search(query, k=k, where_filter=where_filter)

    # ------------------------------------------------------------------
    # Stats
    # ------------------------------------------------------------------

    def count(self) -> int:
        return self._collection.count()

    def stats(self) -> Dict[str, Any]:
        return {
            "collection": settings.chroma_collection,
            "document_count": self.count(),
            "persist_dir": str(settings.chroma_path),
        }
