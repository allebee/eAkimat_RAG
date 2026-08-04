"""Call-center loader — ingests post-processed call transcripts into ChromaDB.

Reads the JSONL produced by scripts/postprocess_call_center.py (after the
evaluator's per-call quality gate). Each useful call yields one document per
qa_pair: the QUESTION is the embedded/searchable text, the ANSWER + context
ride in metadata so retrieval returns them.

Mirrors the contract of video_rag_loader.py so the agent and retrieval code
need no changes — call-center docs join the same ChromaDB collection as a new
source_type="call_center".
"""

from __future__ import annotations

import hashlib
import json
import logging
from pathlib import Path
from typing import Any, Dict, List

logger = logging.getLogger(__name__)

MIN_Q_LENGTH = 10  # skip degenerate questions

# our extracted `modules` -> the metadata `topic` used by context_mapping.py
_MODULE_TO_TOPIC = {
    "budget": "budget_programs",
    "staffing": "staffing",
    "bip": "bip",
    "income": "budget_programs",
    "reports": "monitoring",
    "agreement": "change_requests",
}


def _doc_id(source_file: str, idx: int) -> str:
    raw = f"call_{source_file}_qa_{idx}"
    return f"call_{hashlib.md5(raw.encode()).hexdigest()}"


def _record_to_docs(rec: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Turn one processed call record into a list of ChromaDB documents."""
    if not rec.get("is_useful"):
        return []
    qa_pairs = rec.get("qa_pairs") or []
    if not qa_pairs:
        return []

    source_file = rec.get("source_file", "")
    meta = rec.get("_meta", {}) or {}
    modules = rec.get("modules") or []
    primary_topic = _MODULE_TO_TOPIC.get(modules[0], "") if modules else ""

    docs: List[Dict[str, Any]] = []
    for i, qa in enumerate(qa_pairs):
        question = (qa.get("question") or "").strip()
        answer = (qa.get("answer") or "").strip()
        if len(question) < MIN_Q_LENGTH or not answer:
            continue

        # content = what gets embedded AND returned. Put the answer in the body so
        # the agent has the resolution; lead with the question for retrieval signal.
        content = f"Вопрос: {question}\n\nОтвет: {answer}"

        metadata: Dict[str, Any] = {
            "source_type": "call_center",
            "source_file": source_file,
            "question": question,
            "answer": answer,
            "category": rec.get("category", ""),
            "modules": ",".join(modules),
            "topic": primary_topic,           # for context-page filtering
            "regime": "budget_planning",      # call-center is planning-domain support
            "call_date": meta.get("call_date", rec.get("call_date", "")),
            "confidence": float(rec.get("confidence", 0) or 0),
            "language": rec.get("language", ""),
        }
        docs.append({"id": _doc_id(source_file, i), "content": content, "metadata": metadata})
    return docs


def load_call_center_jsonl(jsonl_path: str | Path) -> List[Dict[str, Any]]:
    """Load all documents from a processed (and gated) call-center JSONL file."""
    path = Path(jsonl_path)
    if not path.exists():
        logger.warning("Call-center JSONL not found: %s", path)
        return []

    all_docs: List[Dict[str, Any]] = []
    n_records = 0
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            rec = json.loads(line)
        except json.JSONDecodeError:
            continue
        if "_error" in rec:
            continue
        n_records += 1
        all_docs.extend(_record_to_docs(rec))

    logger.info("Call-center: %d records -> %d Q&A documents", n_records, len(all_docs))
    return all_docs
