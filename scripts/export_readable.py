"""Export processed call-center records (JSONL) to human-readable .txt files.

Produces, under call_center_transcripts/readable/:
  - one .txt per call (named <date>_<category>_<n>.txt), readable layout
  - _INDEX.txt : one-line summary per call (date | category | problem)
  - _ALL.txt   : everything concatenated into a single readable file

Usage:
  python scripts/export_readable.py
  python scripts/export_readable.py --infile all_processed_ok.jsonl --out readable
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CC = ROOT / "call_center_transcripts"


def safe(s: str, n: int = 40) -> str:
    s = re.sub(r"[^\w\-.]+", "_", (s or "").strip())
    return s[:n].strip("_") or "call"


def render(rec: dict) -> str:
    meta = rec.get("_meta", {}) or {}
    lines = []
    lines.append("=" * 70)
    lines.append(f"Файл звонка : {rec.get('source_file', '')}")
    lines.append(f"Дата        : {meta.get('call_date', rec.get('call_date', '—'))}")
    lines.append(f"Направление : {meta.get('direction', '—')}   Оператор: {meta.get('operator', '—')}")
    lines.append(f"Категория   : {rec.get('category', '—')}")
    lines.append(f"Модули      : {', '.join(rec.get('modules') or []) or '—'}")
    lines.append(f"Язык        : {rec.get('language', '—')}   Уверенность: {rec.get('confidence', '—')}")
    lines.append("=" * 70)
    lines.append("")
    lines.append("ПРОБЛЕМА:")
    lines.append(f"  {rec.get('problem', '') or '—'}")
    lines.append("")
    lines.append("РЕШЕНИЕ:")
    lines.append(f"  {rec.get('resolution', '') or '—'}")
    lines.append("")
    lines.append("ДИАЛОГ (очищенный):")
    for ln in (rec.get("clean_dialogue", "") or "—").split("\n"):
        lines.append(f"  {ln}")
    lines.append("")
    lines.append("ВОПРОСЫ И ОТВЕТЫ (в базе знаний):")
    for i, qa in enumerate(rec.get("qa_pairs") or [], 1):
        lines.append(f"  {i}. В: {qa.get('question', '')}")
        lines.append(f"     О: {qa.get('answer', '')}")
    if rec.get("normalized_terms"):
        terms = [str(t) for t in rec["normalized_terms"] if t]
        lines.append("")
        lines.append("ТЕРМИНЫ: " + ", ".join(terms))
    lines.append("")
    return "\n".join(lines)


def main(args):
    infile = CC / args.infile
    outdir = CC / args.out
    outdir.mkdir(parents=True, exist_ok=True)

    recs = []
    for line in infile.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        r = json.loads(line)
        if "_error" in r or not r.get("is_useful"):
            continue
        recs.append(r)

    index_lines = []
    all_parts = []
    for n, rec in enumerate(recs, 1):
        meta = rec.get("_meta", {}) or {}
        date = meta.get("call_date", rec.get("call_date", "nodate"))
        fname = f"{safe(date,10)}_{safe(rec.get('category',''),30)}_{n:05d}.txt"
        body = render(rec)
        (outdir / fname).write_text(body, encoding="utf-8")
        cat = (rec.get('category') or '—')
        index_lines.append(f"{n:05d} | {date} | {cat:32s} | "
                           f"{(rec.get('problem') or '')[:90]}  -> {fname}")
        all_parts.append(body)

    (outdir / "_INDEX.txt").write_text("\n".join(index_lines), encoding="utf-8")
    (outdir / "_ALL.txt").write_text("\n".join(all_parts), encoding="utf-8")

    print(f"Экспортировано {len(recs)} звонков -> {outdir}")
    print(f"  {len(recs)} отдельных .txt")
    print(f"  _INDEX.txt (оглавление)")
    print(f"  _ALL.txt (всё в одном файле)")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--infile", default="all_processed_ok.jsonl")
    ap.add_argument("--out", default="readable")
    main(ap.parse_args())
