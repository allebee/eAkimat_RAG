#!/usr/bin/env python3
"""RAG Evaluation Script — measures retrieval quality and answer accuracy.

Usage:
    python tests/eval_rag.py
    python tests/eval_rag.py --verbose
    python tests/eval_rag.py --retrieval-only   # Skip LLM, test ChromaDB only
"""

from __future__ import annotations

import argparse
import json
import logging
import sys
import time
from pathlib import Path
from typing import Any, Dict, List

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from dotenv import load_dotenv
load_dotenv()


def evaluate_retrieval(test_cases: List[Dict], verbose: bool = False) -> Dict[str, Any]:
    """Evaluate ChromaDB retrieval quality.

    Measures:
    - Hit Rate: Does the correct topic appear in top-K results?
    - MRR (Mean Reciprocal Rank): How high is the correct result ranked?
    - Context Precision: Of top-K, how many are from correct topic?
    """
    from app.knowledge.chromadb_store import KnowledgeStore
    store = KnowledgeStore.get_instance()

    results = {
        "total": 0,
        "hits": 0,
        "mrr_sum": 0.0,
        "precision_sum": 0.0,
        "with_images": 0,
        "expected_images": 0,
        "details": [],
    }

    kb_cases = [tc for tc in test_cases if tc["module"] == "knowledge_base" and tc.get("expected_topic")]

    for tc in kb_cases:
        results["total"] += 1
        query = tc["question"]
        expected_topic = tc["expected_topic"]
        context_page = tc.get("context_page")

        # Search with context
        docs = store.search_with_context(query, page_context=context_page, k=5)

        # Calculate metrics
        hit = False
        reciprocal_rank = 0.0
        relevant_count = 0
        has_image = False

        for rank, doc in enumerate(docs, 1):
            meta = doc.get("metadata", {})
            doc_topic = meta.get("topic", "")

            if doc_topic == expected_topic:
                if not hit:
                    reciprocal_rank = 1.0 / rank
                    hit = True
                relevant_count += 1

            if meta.get("image_url"):
                has_image = True

        if hit:
            results["hits"] += 1
        results["mrr_sum"] += reciprocal_rank
        results["precision_sum"] += relevant_count / len(docs) if docs else 0

        if tc.get("should_have_media"):
            results["expected_images"] += 1
            if has_image:
                results["with_images"] += 1

        detail = {
            "id": tc["id"],
            "question": query[:60],
            "expected_topic": expected_topic,
            "hit": hit,
            "rr": reciprocal_rank,
            "precision": relevant_count / len(docs) if docs else 0,
            "top_result_topic": docs[0]["metadata"].get("topic", "?") if docs else "none",
            "top_distance": round(docs[0]["distance"], 3) if docs else -1,
            "has_image": has_image,
        }
        results["details"].append(detail)

        if verbose:
            status = "✅" if hit else "❌"
            print(f"  {status} [{tc['id']}] {query[:50]}")
            print(f"     Expected: {expected_topic} | Got: {detail['top_result_topic']} | Dist: {detail['top_distance']}")

    return results


def evaluate_answers(test_cases: List[Dict], verbose: bool = False) -> Dict[str, Any]:
    """Evaluate end-to-end answer quality via the agent.

    Measures:
    - Keyword Hit Rate: Does the answer contain expected keywords?
    - Module Routing: Did the agent use the correct module?
    - Media Inclusion: Did the answer include expected media?
    """
    import asyncio
    from app.agent.graph import run_agent

    results = {
        "total": 0,
        "keyword_hits": 0,
        "keyword_total": 0,
        "module_correct": 0,
        "media_correct": 0,
        "details": [],
    }

    for tc in test_cases:
        results["total"] += 1
        query = tc["question"]
        context_page = tc.get("context_page")

        start = time.time()
        try:
            answer = asyncio.run(run_agent(
                message=query,
                context_page=context_page,
                language="ru",
            ))
        except Exception as exc:
            answer = f"ERROR: {exc}"
        elapsed = time.time() - start

        answer_lower = answer.lower()

        # Keyword matching
        keywords = tc.get("expected_keywords", [])
        matched_keywords = []
        for kw in keywords:
            if kw.lower() in answer_lower:
                matched_keywords.append(kw)
                results["keyword_hits"] += 1
            results["keyword_total"] += 1

        keyword_score = len(matched_keywords) / len(keywords) if keywords else 1.0

        # Media check
        has_media = "[IMAGE:" in answer or "[VIDEO:" in answer or "youtube" in answer_lower
        media_expected = tc.get("should_have_media", False)
        media_correct = (has_media == media_expected)
        if media_correct:
            results["media_correct"] += 1

        # Module routing (heuristic)
        is_analytics = any(x in answer for x in ["тг", "000 000", "бюджет на", "расходы за"])
        expected_analytics = tc["module"] == "analytics"
        module_correct = (is_analytics == expected_analytics)
        if module_correct:
            results["module_correct"] += 1

        detail = {
            "id": tc["id"],
            "question": query[:60],
            "keyword_score": round(keyword_score, 2),
            "matched": matched_keywords,
            "missed": [kw for kw in keywords if kw not in matched_keywords],
            "media_correct": media_correct,
            "module_correct": module_correct,
            "answer_len": len(answer),
            "time_s": round(elapsed, 1),
        }
        results["details"].append(detail)

        if verbose:
            status = "✅" if keyword_score >= 0.5 else "❌"
            print(f"  {status} [{tc['id']}] {query[:50]}")
            print(f"     Keywords: {len(matched_keywords)}/{len(keywords)} | Module: {'✅' if module_correct else '❌'} | Media: {'✅' if media_correct else '❌'} | {elapsed:.1f}s")
            if detail["missed"]:
                print(f"     Missed: {detail['missed']}")

    return results


def print_report(retrieval: Dict, answers: Dict | None = None) -> str:
    """Print and return a formatted evaluation report."""
    lines = []
    lines.append("=" * 65)
    lines.append("  eAkimat365 RAG EVALUATION REPORT")
    lines.append("=" * 65)

    # Retrieval metrics
    total = retrieval["total"]
    if total > 0:
        hit_rate = retrieval["hits"] / total * 100
        mrr = retrieval["mrr_sum"] / total
        precision = retrieval["precision_sum"] / total * 100
        img_rate = retrieval["with_images"] / retrieval["expected_images"] * 100 if retrieval["expected_images"] else 0

        lines.append("")
        lines.append("RETRIEVAL QUALITY (ChromaDB)")
        lines.append("-" * 40)
        lines.append(f"  Hit Rate (top-5):      {retrieval['hits']}/{total}  ({hit_rate:.0f}%)")
        lines.append(f"  MRR (Mean Recip Rank): {mrr:.3f}")
        lines.append(f"  Precision@5:           {precision:.1f}%")
        lines.append(f"  Image Coverage:        {retrieval['with_images']}/{retrieval['expected_images']}  ({img_rate:.0f}%)")

    # Answer quality
    if answers and answers["total"] > 0:
        total_a = answers["total"]
        kw_rate = answers["keyword_hits"] / answers["keyword_total"] * 100 if answers["keyword_total"] else 0
        module_rate = answers["module_correct"] / total_a * 100
        media_rate = answers["media_correct"] / total_a * 100

        lines.append("")
        lines.append("ANSWER QUALITY (End-to-End)")
        lines.append("-" * 40)
        lines.append(f"  Keyword Hit Rate:      {answers['keyword_hits']}/{answers['keyword_total']}  ({kw_rate:.0f}%)")
        lines.append(f"  Module Routing:        {answers['module_correct']}/{total_a}  ({module_rate:.0f}%)")
        lines.append(f"  Media Accuracy:        {answers['media_correct']}/{total_a}  ({media_rate:.0f}%)")

        # Per-case breakdown
        lines.append("")
        lines.append("PER-CASE BREAKDOWN")
        lines.append("-" * 40)
        for d in answers["details"]:
            kw = f"{d['keyword_score']*100:.0f}%"
            mod = "✅" if d["module_correct"] else "❌"
            med = "✅" if d["media_correct"] else "❌"
            lines.append(f"  {d['id']:14s} | KW:{kw:>4s} | Mod:{mod} | Med:{med} | {d['time_s']}s")

    lines.append("")
    lines.append("=" * 65)

    report = "\n".join(lines)
    print(report)
    return report


def main():
    parser = argparse.ArgumentParser(description="Evaluate eAkimat365 RAG system")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose per-case output")
    parser.add_argument("--retrieval-only", action="store_true", help="Only test retrieval (no LLM calls)")
    parser.add_argument("--dataset", default="tests/eval_dataset.json", help="Path to eval dataset")
    parser.add_argument("--output", default="tests/eval_results.json", help="Save results to JSON")
    args = parser.parse_args()

    logging.basicConfig(level=logging.WARNING)

    # Load dataset
    with open(args.dataset, "r", encoding="utf-8") as f:
        test_cases = json.load(f)

    print(f"Loaded {len(test_cases)} test cases\n")

    # Retrieval eval
    print("📊 Evaluating retrieval quality...")
    retrieval = evaluate_retrieval(test_cases, verbose=args.verbose)

    # Answer eval
    answers = None
    if not args.retrieval_only:
        print("\n🤖 Evaluating answer quality (calling LLM)...")
        answers = evaluate_answers(test_cases, verbose=args.verbose)

    # Report
    report = print_report(retrieval, answers)

    # Save results
    output_data = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "dataset_size": len(test_cases),
        "retrieval": retrieval,
    }
    if answers:
        output_data["answers"] = answers

    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2, default=str)
    print(f"\nResults saved to {args.output}")


if __name__ == "__main__":
    main()
