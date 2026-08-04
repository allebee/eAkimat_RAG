"""Evaluator agent for call-center post-processing.

An INDEPENDENT LLM judge scores each rewrite against the raw (Stage-0 cleaned)
transcript. It is adversarial about the failure modes that hurt a RAG index:
  - HALLUCINATION: facts in the rewrite not supported by the raw transcript
  - TERM ERRORS: domain terms left garbled or wrongly "corrected"
  - GATE ERRORS: a useful call marked useless, or garbage marked useful
  - WEAK QA: qa_pairs that aren't self-contained or aren't retrievable

Reads the .jsonl produced by postprocess_call_center.py and emits a verdict +
per-call scores. Exit code 0 if the batch PASSES the quality bar, 1 otherwise —
so a runner can gate the full backfill on it.
"""
from __future__ import annotations

import argparse
import asyncio
import json
import os
import statistics
import sys
from pathlib import Path

from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")

from openai import AsyncOpenAI  # noqa: E402

# provider — grok (default) or gemini (2.5-flash-lite, thinking off)
PROVIDER = os.getenv("EVAL_PROVIDER", "gemini")
if PROVIDER == "gemini":
    MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash-lite")
    client = AsyncOpenAI(api_key=os.getenv("GEMINI_API_KEY"),
                         base_url="https://generativelanguage.googleapis.com/v1beta/openai/")
    EXTRA = {"extra_body": {"extra_body": {"google": {"thinking_config": {"thinking_budget": 0}}}}}
else:
    MODEL = os.getenv("GROK_MODEL", "grok-4-fast-non-reasoning")
    client = AsyncOpenAI(api_key=os.getenv("GROK_API_KEY"), base_url=os.getenv("GROK_BASE_URL"))
    EXTRA = {}

# ---- quality bar to auto-approve the full run ----
PASS_MEAN_OVERALL = 7.0     # mean overall score (out of 10) must be >= this
MAX_HALLUCINATION_RATE = 0.10   # <=10% of calls may have hallucination flag
MAX_GATE_ERROR_RATE = 0.10      # <=10% of calls may have a wrong useful/useless gate
PASS_CALL_OVERALL = 7.0     # per-call gate: a call is indexable if overall >= this AND clean

JUDGE_SYSTEM = """Ты — строгий, но СПРАВЕДЛИВЫЙ независимый эксперт-оценщик. Тебе дают \
(1) СЫРОЙ транскрипт звонка в техподдержку системы eAkimat365 (распознан автоматически, с \
ошибками, смесь русского и казахского) и (2) РЕЗУЛЬТАТ обработки другой моделью (переписанный \
диалог + извлечённые знания). Оцени КАЧЕСТВО ОБРАБОТКИ для базы знаний (RAG).

⚠️ ГЛАВНОЕ: правильно отличай ПЕРЕВОД/ПРОЯСНЕНИЕ от ВЫДУМКИ.
- Задача обрабатывающей модели — ПЕРЕВЕСТИ казахские и искажённые фразы на чистый русский и \
прояснить смысл. Это НЕ выдумка. Пример: сырое «сохраниовт жатпайды» → «не сохраняется» — \
это ПРАВИЛЬНЫЙ перевод, hallucination=false.
- ВЫДУМКА (hallucination=true) — это ТОЛЬКО добавление КОНКРЕТИКИ, которой в звуке НЕ было: \
выдуманные номера программ/спецификаций (напр. «программа 067», когда её не называли), \
выдуманные суммы, ID (AnyDesk), названия организаций, или шаги решения, которые оператор НЕ \
давал. Прежде чем ставить hallucination=true, найди конкретный выдуманный факт и назови его \
в notes. Если не можешь назвать — значит выдумки нет.

Прочие ошибки, опасные для базы знаний:
- ОШИБКИ ТЕРМИНОВ: доменные термины остались искажёнными ИЛИ переведены не полностью \
(в clean_dialogue остался сырой казахский/каша вместо русского).
- ОШИБКА ФИЛЬТРА (gate): полезный звонок помечен бесполезным (is_useful=false), \
ИЛИ мусор/болтовня помечены полезными (is_useful=true).
- СЛАБЫЕ QA: вопросы-ответы не самодостаточны, не отражают звонок, или бесполезны для поиска.

Верни СТРОГО JSON:
{
  "faithfulness": 0-10,        // насколько результат верен сырому транскрипту (10 = ничего не выдумано)
  "term_correction": 0-10,     // насколько правильно исправлены доменные термины
  "dialogue_clarity": 0-10,    // насколько понятен переписанный диалог (для бесполезных звонков ставь 10, если поле пустое уместно)
  "qa_usefulness": 0-10,       // насколько полезны qa_pairs для будущего поиска (для бесполезных звонков ставь N/A → 10, если qa пуст уместно)
  "overall": 0-10,             // общая пригодность для RAG
  "hallucination": true|false, // есть ли выдуманные факты
  "gate_error": true|false,    // неверно определён is_useful
  "verdict": "GOOD" | "ACCEPTABLE" | "BAD",
  "notes": "1-2 предложения: что именно хорошо/плохо"
}"""


def fmt_processed(rec: dict) -> str:
    keep = {k: rec.get(k) for k in
            ("language", "is_useful", "clean_dialogue", "category", "modules",
             "problem", "resolution", "qa_pairs", "normalized_terms", "confidence")}
    return json.dumps(keep, ensure_ascii=False, indent=2)


JUDGE_VOTES = 3  # independent passes per call; aggregate by median / majority


async def _judge_pass(user: str) -> dict | None:
    for attempt in range(4):
        try:
            r = await client.chat.completions.create(
                model=MODEL,
                messages=[{"role": "system", "content": JUDGE_SYSTEM},
                          {"role": "user", "content": user}],
                response_format={"type": "json_object"},
                max_tokens=800,
                **EXTRA,
            )
            return json.loads(r.choices[0].message.content)
        except Exception:
            if attempt == 3:
                return None
            await asyncio.sleep(2 ** attempt)


async def judge_one(sem: asyncio.Semaphore, rec: dict) -> dict:
    raw = rec.get("_raw_cleaned", "")[:6000]
    user = (f"СЫРОЙ ТРАНСКРИПТ:\n\"\"\"\n{raw}\n\"\"\"\n\n"
            f"РЕЗУЛЬТАТ ОБРАБОТКИ:\n{fmt_processed(rec)}")
    async with sem:
        passes = [p for p in await asyncio.gather(*[_judge_pass(user) for _ in range(JUDGE_VOTES)]) if p]
    if not passes:
        return {"source_file": rec.get("source_file"), "_error": "all judge passes failed"}

    def med(key):
        xs = [float(p[key]) for p in passes if isinstance(p.get(key), (int, float))]
        return statistics.median(xs) if xs else None

    # majority vote for boolean flags (kills single-pass false positives)
    def majority(key):
        votes = [bool(p.get(key)) for p in passes]
        return sum(votes) > len(votes) / 2

    v = {
        "source_file": rec.get("source_file"),
        "faithfulness": med("faithfulness"),
        "term_correction": med("term_correction"),
        "dialogue_clarity": med("dialogue_clarity"),
        "qa_usefulness": med("qa_usefulness"),
        "overall": med("overall"),
        "hallucination": majority("hallucination"),
        "gate_error": majority("gate_error"),
        "notes": next((p.get("notes", "") for p in passes if p.get("notes")), ""),
        "_votes": len(passes),
    }
    return v


async def main_async(args):
    in_path = ROOT / "call_center_transcripts" / args.infile
    recs = [json.loads(l) for l in in_path.read_text(encoding="utf-8").splitlines() if l.strip()]
    recs = [r for r in recs if "_error" not in r]
    print(f"Evaluating {len(recs)} processed calls...", file=sys.stderr)
    sem = asyncio.Semaphore(20)
    verdicts = await asyncio.gather(*[judge_one(sem, r) for r in recs])
    verdicts = [v for v in verdicts if v and "_error" not in v]

    def vals(key):
        out = []
        for v in verdicts:
            x = v.get(key)
            if isinstance(x, (int, float)):
                out.append(float(x))
        return out

    mean_overall = statistics.mean(vals("overall")) if vals("overall") else 0
    hall_rate = sum(1 for v in verdicts if v.get("hallucination")) / max(len(verdicts), 1)
    gate_rate = sum(1 for v in verdicts if v.get("gate_error")) / max(len(verdicts), 1)
    counts = {}
    for v in verdicts:
        counts[v.get("verdict", "?")] = counts.get(v.get("verdict", "?"), 0) + 1

    # save full report
    out_path = ROOT / "call_center_transcripts" / args.out
    with open(out_path, "w", encoding="utf-8") as f:
        for v in verdicts:
            f.write(json.dumps(v, ensure_ascii=False) + "\n")

    print("=" * 70, file=sys.stderr)
    print("EVALUATION SUMMARY", file=sys.stderr)
    for k in ("faithfulness", "term_correction", "dialogue_clarity", "qa_usefulness", "overall"):
        vv = vals(k)
        if vv:
            print(f"  mean {k:18s}: {statistics.mean(vv):.2f}", file=sys.stderr)
    print(f"  verdict counts     : {counts}", file=sys.stderr)
    print(f"  hallucination rate : {hall_rate:.0%}", file=sys.stderr)
    print(f"  gate-error rate    : {gate_rate:.0%}", file=sys.stderr)
    print("-" * 70, file=sys.stderr)
    print("  worst calls:", file=sys.stderr)
    for v in sorted(verdicts, key=lambda x: x.get("overall", 0))[:3]:
        print(f"    [{v.get('overall')}] {v.get('source_file','?')[:55]} — {v.get('notes','')[:90]}",
              file=sys.stderr)

    # --- per-call gate: write only judge-clean records to a clean ingest file ---
    if args.filter_out:
        def call_passes(v: dict) -> bool:
            return (not v.get("hallucination")
                    and not v.get("gate_error")
                    and (v.get("overall") or 0) >= PASS_CALL_OVERALL)

        clean_files = {v["source_file"] for v in verdicts if call_passes(v)}
        # only index calls that are also is_useful (skip the useful=false junk)
        clean_recs = [r for r in recs
                      if r.get("source_file") in clean_files and r.get("is_useful")]
        filt_path = ROOT / "call_center_transcripts" / args.filter_out
        with open(filt_path, "w", encoding="utf-8") as f:
            for r in clean_recs:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
        print("-" * 70, file=sys.stderr)
        print(f"  PER-CALL GATE: bar overall>={PASS_CALL_OVERALL}, no hallucination, no gate_error",
              file=sys.stderr)
        print(f"  clean+useful records kept: {len(clean_recs)} / {len(recs)} "
              f"({100*len(clean_recs)/max(len(recs),1):.0f}%) -> {filt_path.name}", file=sys.stderr)

    passed = (mean_overall >= PASS_MEAN_OVERALL
              and hall_rate <= MAX_HALLUCINATION_RATE
              and gate_rate <= MAX_GATE_ERROR_RATE)
    print("=" * 70, file=sys.stderr)
    print(f"  BAR: mean>={PASS_MEAN_OVERALL}, hall<={MAX_HALLUCINATION_RATE:.0%}, gate<={MAX_GATE_ERROR_RATE:.0%}",
          file=sys.stderr)
    print(f"  RESULT: {'PASS ✅' if passed else 'FAIL ❌'}  (report: {out_path})", file=sys.stderr)
    sys.exit(0 if passed else 1)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--infile", default="pilot_20.jsonl")
    ap.add_argument("--out", default="pilot_20_eval.jsonl")
    ap.add_argument("--filter-out", default=None,
                    help="write only judge-clean+useful records to this JSONL (per-call gate)")
    asyncio.run(main_async(ap.parse_args()))
