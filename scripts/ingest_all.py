#!/usr/bin/env python3
"""CLI script to ingest all data into ChromaDB.

Usage:
    python scripts/ingest_all.py
    python scripts/ingest_all.py --clear
    python scripts/ingest_all.py --pdf-dir ./pdf --faq ./prod_data/FAQ.xlsx
"""

from __future__ import annotations

import argparse
import logging
import sys
import time
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from dotenv import load_dotenv
load_dotenv()


def main():
    parser = argparse.ArgumentParser(description="Ingest data into eAkimat365 ChromaDB")
    parser.add_argument("--pdf-dir", default="./pdf", help="Path to PDF directory")
    parser.add_argument("--faq", default="./prod_data/FAQ.xlsx", help="Path to FAQ Excel file")
    parser.add_argument(
        "--instructions", default="./prod_data/instructions.xlsx",
        help="Path to instructions Excel file",
    )
    parser.add_argument("--clear", action="store_true", help="Clear existing data before ingesting")
    parser.add_argument("--faq-only", action="store_true", help="Only ingest FAQ (skip PDFs)")
    parser.add_argument("--pdf-only", action="store_true", help="Only ingest PDFs (skip FAQ)")
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
    )
    logger = logging.getLogger("ingest")

    start_time = time.time()

    # Initialize store
    from app.knowledge.chromadb_store import KnowledgeStore
    store = KnowledgeStore.get_instance()

    if args.clear:
        logger.info("Clearing existing ChromaDB data...")
        store.clear()

    total_docs = 0

    # --- FAQ ---
    if not args.pdf_only:
        logger.info("=" * 60)
        logger.info("STEP 1: Loading FAQ from %s", args.faq)
        logger.info("=" * 60)

        from app.ingestion.faq_loader import load_faq
        faq_docs = load_faq(args.faq)

        if faq_docs:
            store.add_documents(
                texts=[d["content"] for d in faq_docs],
                metadatas=[d["metadata"] for d in faq_docs],
                ids=[d["id"] for d in faq_docs],
            )
            total_docs += len(faq_docs)
            logger.info("✅ Ingested %d FAQ documents", len(faq_docs))
        else:
            logger.warning("⚠️  No FAQ documents loaded")

    # --- PDFs ---
    if not args.faq_only:
        logger.info("=" * 60)
        logger.info("STEP 2: Processing PDFs from %s", args.pdf_dir)
        logger.info("=" * 60)

        pdf_dir = Path(args.pdf_dir)
        if not pdf_dir.exists():
            logger.warning("⚠️  PDF directory not found: %s", pdf_dir)
        else:
            from app.ingestion.deduplicator import deduplicate_pdfs
            from app.ingestion.pdf_loader import PDFLoader

            unique_pdfs = deduplicate_pdfs(pdf_dir)
            logger.info("Found %d unique PDFs (after deduplication)", len(unique_pdfs))

            loader = PDFLoader()
            for i, pdf_info in enumerate(unique_pdfs, 1):
                logger.info(
                    "[%d/%d] Processing: %s",
                    i, len(unique_pdfs), pdf_info["title"],
                )
                chunks = loader.load_pdf(pdf_info["path"], title=pdf_info["title"])
                if chunks:
                    store.add_documents(
                        texts=[c["content"] for c in chunks],
                        metadatas=[c["metadata"] for c in chunks],
                        ids=[c["id"] for c in chunks],
                    )
                    total_docs += len(chunks)
                    logger.info("  → %d chunks", len(chunks))

    # --- Instructions (navigation tree) ---
    if not args.pdf_only and not args.faq_only:
        logger.info("=" * 60)
        logger.info("STEP 3: Building navigation tree")
        logger.info("=" * 60)

        instructions_path = Path(args.instructions)
        if instructions_path.exists():
            from app.ingestion.instructions_loader import load_instructions, save_navigation_tree
            entries = load_instructions(str(instructions_path))
            if entries:
                save_navigation_tree(entries, "data/navigation_tree.json")
                logger.info("✅ Navigation tree saved (%d entries)", len(entries))
        else:
            logger.warning("⚠️  Instructions file not found: %s", instructions_path)

    # --- Summary ---
    elapsed = time.time() - start_time
    logger.info("=" * 60)
    logger.info("INGESTION COMPLETE")
    logger.info("  Total documents in ChromaDB: %d", store.count())
    logger.info("  Documents added this run: %d", total_docs)
    logger.info("  Time elapsed: %.1f seconds", elapsed)
    logger.info("=" * 60)


if __name__ == "__main__":
    main()
