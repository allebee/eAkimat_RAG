#!/usr/bin/env python3
"""CLI script to ingest all data into ChromaDB.

Usage:
    python scripts/ingest_all.py
    python scripts/ingest_all.py --clear
    python scripts/ingest_all.py --pdf-dir ./pdf --faq ./prod_data/FAQ.xlsx
    python scripts/ingest_all.py --video-only
    python scripts/ingest_all.py --pdf-instructions-only
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
    parser.add_argument(
        "--video-dir", default="./video_instructions/output_dataset",
        help="Path to video RAG dataset directory (with _rag.json files)",
    )
    parser.add_argument(
        "--pdf-instructions-dir", default="./pdf_instructions",
        help="Path to new clean PDF instructions directory",
    )
    parser.add_argument(
        "--calls-dir", default="./MP3toTXT",
        help="Path to directory with Whisper-transcribed support calls (.txt)",
    )
    parser.add_argument(
        "--calls-no-llm", action="store_true",
        help="Skip Grok cleaning for calls; ingest raw transcripts only (debug)",
    )
    parser.add_argument("--clear", action="store_true", help="Clear existing data before ingesting")
    parser.add_argument("--faq-only", action="store_true", help="Only ingest FAQ")
    parser.add_argument("--pdf-only", action="store_true", help="Only ingest PDFs (original)")
    parser.add_argument("--video-only", action="store_true", help="Only ingest video RAG data")
    parser.add_argument("--pdf-instructions-only", action="store_true", help="Only ingest new PDF instructions")
    parser.add_argument("--calls-only", action="store_true", help="Only ingest support call transcripts")
    parser.add_argument(
        "--call-center-jsonl",
        default="./call_center_transcripts/all_processed_clean.jsonl",
        help="Path to gated, post-processed call-center JSONL (from postprocess+evaluate)",
    )
    parser.add_argument(
        "--call-center-only", action="store_true",
        help="Only ingest post-processed call-center Q&A (gated JSONL)",
    )
    args = parser.parse_args()

    # Determine what to ingest
    ingest_all = not any([
        args.faq_only, args.pdf_only, args.video_only,
        args.pdf_instructions_only, args.calls_only, args.call_center_only,
    ])

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

    # --- STEP 1: FAQ ---
    if ingest_all or args.faq_only:
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

    # --- STEP 2: Original PDFs ---
    if ingest_all or args.pdf_only:
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

    # --- STEP 3: Navigation tree ---
    if ingest_all:
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

    # --- STEP 4: Video RAG (transcriptions + frames) ---
    if ingest_all or args.video_only:
        logger.info("=" * 60)
        logger.info("STEP 4: Loading Video RAG data from %s", args.video_dir)
        logger.info("=" * 60)

        from app.ingestion.video_rag_loader import load_all_video_rag
        video_docs = load_all_video_rag(args.video_dir)

        if video_docs:
            # Batch upsert in chunks of 100 to avoid memory issues
            batch_size = 100
            for batch_start in range(0, len(video_docs), batch_size):
                batch = video_docs[batch_start:batch_start + batch_size]
                store.add_documents(
                    texts=[d["content"] for d in batch],
                    metadatas=[d["metadata"] for d in batch],
                    ids=[d["id"] for d in batch],
                )
            total_docs += len(video_docs)
            logger.info("✅ Ingested %d video RAG documents", len(video_docs))
        else:
            logger.warning("⚠️  No video RAG documents loaded")

    # --- STEP 5: New PDF instructions (from analyst) ---
    if ingest_all or args.pdf_instructions_only:
        logger.info("=" * 60)
        logger.info("STEP 5: Processing new PDF instructions from %s", args.pdf_instructions_dir)
        logger.info("=" * 60)

        pdf_instr_dir = Path(args.pdf_instructions_dir)
        if not pdf_instr_dir.exists():
            logger.warning("⚠️  PDF instructions directory not found: %s", pdf_instr_dir)
        else:
            from app.ingestion.pdf_loader import PDFLoader

            pdf_files = sorted(pdf_instr_dir.glob("*.pdf"))
            logger.info("Found %d PDF instruction files", len(pdf_files))

            loader = PDFLoader()
            for i, pdf_path in enumerate(pdf_files, 1):
                title = pdf_path.stem
                logger.info("[%d/%d] Processing: %s", i, len(pdf_files), title)
                chunks = loader.load_pdf(str(pdf_path), title=title)
                if chunks:
                    # Tag as pdf_instruction to differentiate
                    for c in chunks:
                        c["metadata"]["source_type"] = "pdf_instruction"
                    store.add_documents(
                        texts=[c["content"] for c in chunks],
                        metadatas=[c["metadata"] for c in chunks],
                        ids=[c["id"] for c in chunks],
                    )
                    total_docs += len(chunks)
                    logger.info("  → %d chunks", len(chunks))

    # --- STEP 6: Support call transcripts ---
    if ingest_all or args.calls_only:
        logger.info("=" * 60)
        logger.info("STEP 6: Loading support calls from %s", args.calls_dir)
        logger.info("=" * 60)

        from app.ingestion.call_loader import load_all_calls
        call_docs = load_all_calls(
            args.calls_dir,
            use_llm=not args.calls_no_llm,
        )

        if call_docs:
            batch_size = 100
            for batch_start in range(0, len(call_docs), batch_size):
                batch = call_docs[batch_start:batch_start + batch_size]
                store.add_documents(
                    texts=[d["content"] for d in batch],
                    metadatas=[d["metadata"] for d in batch],
                    ids=[d["id"] for d in batch],
                )
            total_docs += len(call_docs)
            logger.info("✅ Ingested %d support-call documents", len(call_docs))
        else:
            logger.warning("⚠️  No support-call documents loaded")

    if ingest_all or args.call_center_only:
        logger.info("=" * 60)
        logger.info("STEP 7: Loading post-processed call-center Q&A from %s", args.call_center_jsonl)
        logger.info("=" * 60)

        from app.ingestion.call_center_loader import load_call_center_jsonl
        cc_docs = load_call_center_jsonl(args.call_center_jsonl)

        if cc_docs:
            batch_size = 200
            for batch_start in range(0, len(cc_docs), batch_size):
                batch = cc_docs[batch_start:batch_start + batch_size]
                store.add_documents(
                    texts=[d["content"] for d in batch],
                    metadatas=[d["metadata"] for d in batch],
                    ids=[d["id"] for d in batch],
                )
            total_docs += len(cc_docs)
            logger.info("✅ Ingested %d call-center Q&A documents", len(cc_docs))
        else:
            logger.warning("⚠️  No call-center Q&A documents loaded (run postprocess+evaluate first)")

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
