"""Re-embed the existing ChromaDB collection with the currently-configured
embedding provider (BGE), WITHOUT re-running the source loaders.

Why: switching embeddings changes the vector dimension, so every stored vector
must be regenerated. The documents + metadata already live in ChromaDB, so we
read them straight out, wipe the collection, and re-add them — the model that
KnowledgeStore builds (selected by EMBEDDING_PROVIDER) produces the new vectors.

Safe to interrupt: chroma_data was backed up before this runs. Idempotent enough
to re-run from scratch.

Run:  EMBEDDING_PROVIDER=bge ./venv/bin/python scripts/reembed_bge.py
"""

from __future__ import annotations

import sys
import time

from app.config import settings
from app.knowledge.chromadb_store import KnowledgeStore

BATCH = 256


def main() -> int:
    print(f"Embedding provider: {settings.embedding_provider}")
    if settings.embedding_provider != "bge":
        print("Refusing to run: EMBEDDING_PROVIDER is not 'bge'. Set it first.")
        return 1

    store = KnowledgeStore.get_instance()  # loads the BGE model here

    # 1. Read everything currently stored (no embedding needed for a get()).
    existing = store._collection.get(include=["documents", "metadatas"])
    ids = existing["ids"]
    docs = existing["documents"]
    metas = existing["metadatas"]
    total = len(ids)
    print(f"Read {total} documents from existing collection.")
    if total == 0:
        print("Nothing to re-embed. Aborting.")
        return 1

    # 2. Wipe the collection so the new (different-dim) vectors can be written.
    store.clear()
    print("Collection cleared. Re-embedding with BGE ...")

    # 3. Re-add in batches — add_documents() embeds with the BGE backend.
    t0 = time.time()
    done = 0
    for i in range(0, total, BATCH):
        store.add_documents(
            texts=docs[i : i + BATCH],
            metadatas=metas[i : i + BATCH],
            ids=ids[i : i + BATCH],
        )
        done += len(ids[i : i + BATCH])
        elapsed = time.time() - t0
        rate = done / elapsed if elapsed else 0
        print(f"  {done}/{total}  ({rate:.0f} docs/s)", flush=True)

    final = store.count()
    print(f"Done. Collection now has {final} documents (was {total}).")
    return 0 if final == total else 2


if __name__ == "__main__":
    sys.exit(main())
