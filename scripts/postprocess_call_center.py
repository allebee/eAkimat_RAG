"""Call-center transcript post-processing: rewrite garbled STT into clean,
understandable, RAG-ingestible knowledge using grok-4-fast-non-reasoning.

Pipeline:
  Stage 0 (free)  — deterministic pre-clean: strip BOM, drop timestamp markers,
                    kill Whisper hallucinations, collapse verbatim repetition,
                    parse filename metadata, drop too-short files.
  Stage 1 (LLM)   — rewrite into clean speaker-separated dialogue + structured
                    extraction (problem / resolution / qa_pairs / modules / ...).

Usage:
  python scripts/postprocess_call_center.py --limit 20 --sample --out pilot.jsonl
  python scripts/postprocess_call_center.py --all --out all_processed.jsonl
"""
from __future__ import annotations

import argparse
import asyncio
import json
import os
import random
import re
import sys
import time
from pathlib import Path

from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")

from openai import AsyncOpenAI  # noqa: E402

# --- provider config (set by configure_provider from --provider) ---
MODEL = os.getenv("GROK_MODEL", "grok-4-fast-non-reasoning")
BASE_URL = os.getenv("GROK_BASE_URL", "https://api.x.ai/v1")
API_KEY = os.getenv("GROK_API_KEY", "")
EXTRA_BODY: dict = {}     # provider-specific request extras (e.g. Gemini thinking-off)
PRICE_IN = 0.20e-6        # grok-4-fast defaults; overridden per provider
PRICE_OUT = 0.50e-6


def configure_provider(provider: str) -> None:
    """Point the client at grok (default) or gemini (2.5-flash-lite, thinking off)."""
    global MODEL, BASE_URL, API_KEY, EXTRA_BODY, PRICE_IN, PRICE_OUT
    if provider == "gemini":
        MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash-lite")
        BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
        API_KEY = os.getenv("GEMINI_API_KEY", "")
        # disable thinking → reliable JSON, far cheaper output.
        # splatted as **EXTRA_BODY → the .create() kwarg `extra_body` must itself
        # carry Gemini's passthrough {"extra_body": {"google": {...}}}.
        EXTRA_BODY = {"extra_body": {"extra_body": {"google": {"thinking_config": {"thinking_budget": 0}}}}}
        PRICE_IN, PRICE_OUT = 0.10e-6, 0.40e-6   # gemini-2.5-flash-lite tier
    else:  # grok
        MODEL = os.getenv("GROK_MODEL", "grok-4-fast-non-reasoning")
        BASE_URL = os.getenv("GROK_BASE_URL", "https://api.x.ai/v1")
        API_KEY = os.getenv("GROK_API_KEY", "")
        EXTRA_BODY = {}
        PRICE_IN, PRICE_OUT = 0.20e-6, 0.50e-6


TRANSCRIPT_DIRS = [
    ROOT / "call_center_transcripts" / "transcripts",
    ROOT / "call_center_transcripts" / "transcripts 2",
    ROOT / "call_center_transcripts" / "transcripts 3",
]
MIN_BYTES = 150          # Stage-0 drop threshold
MAX_CONCURRENCY = 20     # async semaphore size (respect provider rate limit)

# ---------- STAGE 0: deterministic pre-clean ----------
_HALLUCINATIONS = [
    r"Субтитры (?:сделал|создавал|подготовил|редактировал).*",
    r"Редактор субтитров.*",
    r"Корректор.*",
    r"Продолжение следует\.{0,3}",
    r"Спасибо за просмотр\.?",
    r"DimaTorzok",
]
_HALL_RE = re.compile("|".join(_HALLUCINATIONS), re.IGNORECASE)
_TS_RE = re.compile(r"\[\d+\.\d+\s*-\s*\d+\.\d+\]")

# Long runs of spelled-out digit words = a dictated access code / ID, almost always
# mis-recognized. Replace with a neutral placeholder so the LLM can't fabricate a
# clean-but-wrong ID out of them. (Russian + Kazakh number words.)
_DIGIT_WORDS = (r"ноль|один|одинн|два|две|три|четыре|пять|шесть|семь|восемь|девять|"
                r"десять|сто|двести|триста|сорок|пятьдесят|шестьдесят|семьдесят|"
                r"восемьдесят|девяносто|двадцать|тридцать|сотен|тысяч[а-я]*|"
                r"шестьсот|семьсот|восемьсот|девятьсот|пятьсот|четыреста|"
                r"бір|екі|үш|төрт|бес|алты|жеті|сегіз|тоғыз|он|жүз|мың|жиырма|отыз|елу|алпыс|жетпіс")
# 5+ consecutive number-words → a dictated code; collapse to a marker.
_DICTATED_CODE_RE = re.compile(
    rf"(?:\b(?:{_DIGIT_WORDS})\b[\s,.-]*){{5,}}", re.IGNORECASE)


# Garbled remote-access brand mentions → neutral phrase, so the LLM names a generic
# "remote access" tool instead of confidently fabricating "AnyDesk" + a (wrong) ID.
_REMOTE_RE = re.compile(
    r"\b(?:any\s?desk|анидеск|ани\s?доск|анидоск|адинаск|анидес[кq]а?|кажтянадуст|"
    r"тим\s?вью?вер|teamviewer)\b", re.IGNORECASE)


def stage0(text: str) -> str:
    text = text.lstrip("﻿")
    text = _TS_RE.sub(" ", text)
    text = _HALL_RE.sub(" ", text)
    text = _DICTATED_CODE_RE.sub(" [продиктован код/ID] ", text)  # neutralize dictated codes
    text = _REMOTE_RE.sub(" программа удалённого доступа ", text)  # neutralize brand guess
    text = re.sub(r"\b(\S+\s+)\1{2,}", r"\1", text)  # collapse verbatim repetition
    return re.sub(r"\s+", " ", text).strip()


def parse_meta(name: str) -> dict:
    # Format A: DD-MM-YYYY_HH-MM_<phone>_<direction>_<phone?>_user_<operator>.txt
    m = re.match(
        r"(\d{2}-\d{2}-\d{4})_(\d{2}-\d{2})_\d+_([a-zA-Z]+)_\d*_user_(.+)\.txt", name
    )
    if m:
        d, t, direction, op = m.groups()
        dd, mm, yyyy = d.split("-")
        return {"call_date": f"{yyyy}-{mm}-{dd}", "direction": direction, "operator": op.strip()}
    # Format B (MP3toTXT): YYYY-MM-DD_HH-MM_<phone>_<id>.txt
    m = re.match(r"(\d{4}-\d{2}-\d{2})_(\d{2}-\d{2})_", name)
    if m:
        return {"call_date": m.group(1), "direction": "?", "operator": "?"}
    return {"call_date": "?", "direction": "?", "operator": "?"}


# ---------- STAGE 1: LLM rewrite + structure ----------
SYSTEM = """Ты — аналитик службы поддержки государственной системы бюджетного планирования \
eAkimat365 (Казахстан). Тебе дают СЫРОЙ автоматический транскрипт телефонного звонка в \
техподдержку. Транскрипт получен акустической моделью без пунктуации, без разделения \
говорящих, с ошибками распознавания, и содержит смесь русского и казахского языков \
(часто в одном предложении).

ТВОЯ ЗАДАЧА: переписать звонок в понятный вид и извлечь знания.

ДВЕ ОДИНАКОВО ВАЖНЫЕ ЗАДАЧИ — НЕ ЖЕРТВУЙ НИ ОДНОЙ:

(1) ПОЛНОСТЬЮ ПЕРЕВЕДИ И ПОЧИСТИ. clean_dialogue должен быть полностью на ЧИСТОМ РУССКОМ \
языке, с пунктуацией и разделением говорящих. Казахские фразы ОБЯЗАТЕЛЬНО переводи на \
русский (напр. «программа удалённого доступа кіре аласыз ба» → «можете подключиться через \
программу удалённого доступа?», «сохраниовт жатпайды» → «не сохраняется»). НЕ оставляй \
сырой казахский/искажённый текст как есть — это и есть твоя работа. НЕ называй конкретные \
бренды (AnyDesk, TeamViewer) — пиши «программа удалённого доступа».

(2) НИЧЕГО НЕ ВЫДУМЫВАЙ. Переводи и проясняй смысл, но НЕ добавляй факты, которых нет:
- Запрещено придумывать номера программ/спецификаций, суммы, ID (AnyDesk и т.п.), названия \
организаций, шаги решения, если их НЕТ в тексте.
- Число в тексте («шестьсот пятьдесят семь») переписывай как число (657). НЕ превращай \
произвольное число в «программу 067».
- qa_pairs — ТОЛЬКО из того, что оператор реально объяснил. Нет решения → qa_pairs пустой, \
resolution пустой. НЕ сочиняй «типовой правильный ответ».
- Частично понятный звонок: переведи понятное, не дополняй догадками, confidence 0.3-0.5.

Различай: ПЕРЕВОД смысла «не сохраняется план финансирования» — это НЕ выдумка, это твоя \
работа. ВЫДУМКА — это добавление конкретики (номер 067, ID, сумма), которой в звуке не было.

🔴 ОСОБОЕ ПРАВИЛО ПРО ИСКАЖЁННЫЕ СЛОВА И ЧИСЛА (частая ошибка — не повторяй её):
- Если непонятное искажённое слово ПОХОЖЕ на название программы/сервиса (напр. \
«кажтянадуст», «анидеск», «адинаск»), НЕ заменяй его уверенно на «AnyDesk», «ИПРОМ» и т.п. \
Пиши обобщённо: «удалённый доступ», «программа удалённого доступа», или оставь как \
[неразборчиво]. НЕ присваивай конкретное название/бренд, если не уверен.
- Продиктованные по цифрам числа (ID, коды) почти всегда распознаны НЕВЕРНО. НЕ записывай \
их как точный ID и НЕ называй «ID AnyDesk: 198-676-940». Вместо этого пиши: «оператор \
продиктовал ID для удалённого подключения» БЕЗ самих цифр, либо цифры пометь как \
ненадёжные. Лучше опустить число, чем дать ложно-точное.
- Если звонок — это ТОЛЬКО диктовка кода удалённого доступа без описания проблемы — \
is_useful=false. Но если у пользователя есть понятная проблема (не могу войти, забыл \
пароль, не сохраняется, где найти раздел) — звонок ПОЛЕЗЕН (is_useful=true), даже когда \
для её решения оператор предложил удалённый доступ.

Если звонок бесполезен (тишина, "алло", ошиблись номером, "подождите на линии", \
болтовня без сути) — пометь is_useful=false и оставь пустые поля \
clean_dialogue/problem/resolution/qa_pairs.

СЛОВАРЬ ИСПРАВЛЕНИЙ РАСПОЗНАВАНИЯ — применяй ТОЛЬКО когда в тексте действительно звучит \
искажённый термин из левой части. НЕ вставляй термин из правой части, если соответствующего \
искажения в транскрипте нет:
  госарқтрог / госконтролья → госконтроль;  госупреждение → госучреждение
  спетивка / спетивкадан / спетивик / спетивкаф / специфика → спецификация
  штатка → штатное расписание (штатка)
  бип → БИП (бюджетные инвестиционные проекты)
  заявкаде / заявкаха / анедетупрема → бюджетная заявка
  патограмма / патограмм → подпрограмма;  гу → ГУ (государственное учреждение)
  ВНИМАНИЕ ПРО НОМЕРА ПРОГРАММ/СПЕЦИФИКАЦИЙ: если в тексте звучит «программа ноль \
шестьдесят семь» — это программа 067; но просто число (657, 311 и т.п.) переписывай как \
число, НЕ называй его «программой 067». Не выдумывай номер программы, если его не назвали.
  отчёт о сети штатах и контингентах → отчёт о сети, штатах и контингентах
  холменстит / холменститен → утверждает / не утверждает (статус согласования)
  перезахранят / перезахранятетпеген → пересохранить / не пересохраняется
  свод / сводке → свод (консолидация)

Верни СТРОГО JSON по схеме:
{
  "language": "ru" | "kk" | "mixed",
  "is_useful": true | false,
  "clean_dialogue": "переписанный диалог с разделением говорящих (Оператор: / Клиент:), \
исправленными терминами и пунктуацией — связный понятный текст",
  "category": "короткий машинный ярлык на английском, snake_case",
  "modules": ["budget"|"staffing"|"bip"|"income"|"reports"|"agreement"|"other"],
  "problem": "1-2 предложения: в чём проблема пользователя (чистый русский)",
  "resolution": "что ответил/сделал оператор (или пустая строка)",
  "qa_pairs": [{"question": "как спросил бы пользователь в чат-боте", "answer": "пошаговый конкретный ответ"}],
  "normalized_terms": ["исправленные доменные термины"],
  "confidence": 0.0
}
Пиши clean_dialogue/problem/resolution/qa_pairs на чистом русском, даже если оригинал \
был казахский или смешанный — это язык поиска в базе знаний."""


def build_user(cleaned: str, meta: dict) -> str:
    return (
        f"Метаданные звонка:\n  дата: {meta['call_date']}\n  направление: {meta['direction']}\n"
        f"  оператор: {meta['operator']}\n\nСЫРОЙ ТРАНСКРИПТ:\n\"\"\"\n{cleaned}\n\"\"\""
    )


# ---------- STAGE 1b: grounding-only self-critique pass ----------
# Cheap second Grok-fast call. Its ONLY job: remove/generalize specifics in the
# draft that are NOT literally supported by the raw transcript. It must NOT
# re-summarize or add anything — that would re-introduce hallucination.
CRITIC_SYSTEM = """Ты — редактор-фактчекер. Тебе дают (1) СЫРОЙ транскрипт звонка и \
(2) ЧЕРНОВИК его обработки (JSON). Твоя ЕДИНСТВЕННАЯ задача — убрать из черновика \
ВЫДУМАННУЮ конкретику, которой НЕТ в сыром транскрипте. Ничего не добавляй и не \
пересказывай заново.

Проверь каждый КОНКРЕТНЫЙ факт в черновике (clean_dialogue, problem, resolution, qa_pairs):
- Номера программ/спецификаций/форм (067, 113, 51-90 …), точные суммы, ID удалённого \
доступа (AnyDesk и т.п.), названия брендов/сервисов, названия организаций.
- Если факт ЕСТЬ в сыром тексте (пусть искажённо) — оставь.
- Если факта НЕТ в сыром тексте — УДАЛИ его или замени на обобщение («удалённый доступ» \
вместо «AnyDesk 198-676-940»; «нужная сумма» вместо выдуманного числа; убери выдуманный \
номер программы). Продиктованные по цифрам коды/ID удаляй (они почти всегда искажены).
- Если после удаления выдумок в qa_pairs не осталось реального решения от оператора — \
сделай qa_pairs=[] и resolution="". Но problem и clean_dialogue ОСТАВЬ (они полезны).

⚠️ НЕ МЕНЯЙ is_useful с true на false без крайней необходимости. Звонок ПОЛЕЗЕН, даже если \
оператор не дал решения, но в нём есть понятная проблема пользователя (не могу войти / \
забыл пароль / не сохраняется / не могу добавить позицию / где найти раздел). Такие звонки \
ценны: проблема пользователя — это знание для базы. Ставь is_useful=false ТОЛЬКО для явного \
мусора (тишина, «алло», ошиблись номером, болтовня без сути, чистая диктовка кода доступа).

Сохрани ТУ ЖЕ JSON-схему (все поля). Верни ИСПРАВЛЕННЫЙ JSON целиком."""


async def critique(client: AsyncOpenAI, draft: dict, cleaned: str) -> dict:
    """Second pass: strip invented specifics. Returns corrected draft (or draft on failure)."""
    draft_view = {k: draft.get(k) for k in
                  ("language", "is_useful", "clean_dialogue", "category", "modules",
                   "problem", "resolution", "qa_pairs", "normalized_terms", "confidence")}
    user = (f"СЫРОЙ ТРАНСКРИПТ:\n\"\"\"\n{cleaned}\n\"\"\"\n\n"
            f"ЧЕРНОВИК ОБРАБОТКИ:\n{json.dumps(draft_view, ensure_ascii=False, indent=2)}")
    for attempt in range(3):
        try:
            r = await client.chat.completions.create(
                model=MODEL,
                messages=[{"role": "system", "content": CRITIC_SYSTEM},
                          {"role": "user", "content": user}],
                response_format={"type": "json_object"},
                max_tokens=4000,
                **EXTRA_BODY,
            )
            fixed = json.loads(r.choices[0].message.content)
            # preserve bookkeeping fields, accumulate token usage
            fixed["source_file"] = draft.get("source_file")
            fixed["_meta"] = draft.get("_meta")
            fixed["_raw_cleaned"] = cleaned
            u = draft.get("_usage", {"in": 0, "out": 0})
            fixed["_usage"] = {"in": u["in"] + r.usage.prompt_tokens,
                               "out": u["out"] + r.usage.completion_tokens}
            return fixed
        except Exception:
            if attempt == 2:
                return draft  # critique failed → keep the draft
            await asyncio.sleep(2 ** attempt)
    return draft


async def process_one(client: AsyncOpenAI, sem: asyncio.Semaphore, path: Path,
                      two_pass: bool = False) -> dict | None:
    raw = path.read_text(encoding="utf-8", errors="replace")
    if len(raw.encode("utf-8")) < MIN_BYTES:
        return None  # Stage-0 drop: empty / too short
    cleaned = stage0(raw)
    if len(cleaned) < 40:
        return None
    meta = parse_meta(path.name)
    user = build_user(cleaned, meta)
    async with sem:
        draft = None
        for attempt in range(4):
            try:
                r = await client.chat.completions.create(
                    model=MODEL,
                    messages=[{"role": "system", "content": SYSTEM},
                              {"role": "user", "content": user}],
                    response_format={"type": "json_object"},
                    max_tokens=4000,
                    **EXTRA_BODY,
                )
                draft = json.loads(r.choices[0].message.content)
                draft["source_file"] = path.name
                draft["_meta"] = meta
                draft["_usage"] = {"in": r.usage.prompt_tokens, "out": r.usage.completion_tokens}
                draft["_raw_cleaned"] = cleaned
                break
            except Exception as e:
                if attempt == 3:
                    return {"source_file": path.name, "_error": str(e)}
                await asyncio.sleep(2 ** attempt)
        if draft is None:
            return {"source_file": path.name, "_error": "no draft"}
        # Stage 1b: only critique calls that produced content (skip useless ones — nothing to strip)
        if two_pass and draft.get("is_useful"):
            draft = await critique(client, draft, cleaned)
        return draft


def gather_files(sample: bool, limit: int | None) -> list[Path]:
    # The 3 transcript folders overlap heavily: the same call appears under the
    # same filename in multiple folders with IDENTICAL content. Dedup by filename
    # (keep first occurrence) so each unique call is processed exactly once.
    seen: set[str] = set()
    files: list[Path] = []
    for d in TRANSCRIPT_DIRS:
        if d.exists():
            for f in sorted(d.glob("*.txt")):
                if f.name not in seen:
                    seen.add(f.name)
                    files.append(f)
    if sample:
        rng = random.Random(42)  # deterministic sample for reproducibility
        rng.shuffle(files)
    if limit:
        files = files[:limit]
    return files


async def main_async(args):
    files = gather_files(args.sample, args.limit)
    out_path = ROOT / "call_center_transcripts" / args.out

    # resume: skip files already in the output (crash-safe for the 17K run)
    done: set[str] = set()
    if out_path.exists():
        for line in out_path.read_text(encoding="utf-8").splitlines():
            try:
                done.add(json.loads(line).get("source_file"))
            except Exception:
                pass
    todo = [f for f in files if f.name not in done]
    print(f"Processing {len(todo)} files ({len(done)} already done) "
          f"(concurrency={MAX_CONCURRENCY}, two_pass={args.two_pass}, model={MODEL})...",
          file=sys.stderr)

    client = AsyncOpenAI(api_key=API_KEY, base_url=BASE_URL)
    sem = asyncio.Semaphore(MAX_CONCURRENCY)
    t0 = time.time()

    # stream results to disk as each completes (append mode); progress every 250
    counters = {"kept": 0, "useful": 0, "err": 0, "drop": 0, "in": 0, "out": 0, "n": 0}
    write_lock = asyncio.Lock()
    fh = open(out_path, "a", encoding="utf-8")

    async def run(f: Path):
        r = await process_one(client, sem, f, two_pass=args.two_pass)
        async with write_lock:
            counters["n"] += 1
            if r is None:
                counters["drop"] += 1
            elif "_error" in r:
                counters["err"] += 1
                fh.write(json.dumps(r, ensure_ascii=False) + "\n")
            else:
                counters["kept"] += 1
                if r.get("is_useful"):
                    counters["useful"] += 1
                counters["in"] += r["_usage"]["in"]
                counters["out"] += r["_usage"]["out"]
                fh.write(json.dumps(r, ensure_ascii=False) + "\n")
            if counters["n"] % 250 == 0:
                fh.flush()
                cost = counters["in"] * PRICE_IN + counters["out"] * PRICE_OUT
                el = time.time() - t0
                rate = counters["n"] / el if el else 0
                eta = (len(todo) - counters["n"]) / rate if rate else 0
                print(f"  [{counters['n']}/{len(todo)}] kept={counters['kept']} "
                      f"useful={counters['useful']} drop={counters['drop']} err={counters['err']} "
                      f"${cost:.2f} {rate:.1f}/s ETA {eta/60:.0f}m", file=sys.stderr)

    await asyncio.gather(*[run(f) for f in todo])
    fh.flush(); fh.close()
    dt = time.time() - t0
    cost = counters["in"] * PRICE_IN + counters["out"] * PRICE_OUT

    print("=" * 70, file=sys.stderr)
    print(f"  files this run  : {len(todo)} (+{len(done)} resumed)", file=sys.stderr)
    print(f"  Stage-0 dropped : {counters['drop']}", file=sys.stderr)
    print(f"  LLM errors      : {counters['err']}", file=sys.stderr)
    print(f"  LLM processed   : {counters['kept']}", file=sys.stderr)
    print(f"  is_useful=true  : {counters['useful']} "
          f"({100*counters['useful']/max(counters['kept'],1):.0f}%)", file=sys.stderr)
    print(f"  tokens          : {counters['in']} in / {counters['out']} out", file=sys.stderr)
    print(f"  cost (this run) : ${cost:.4f}", file=sys.stderr)
    print(f"  wall time       : {dt/60:.1f}m", file=sys.stderr)
    print(f"  written         : {out_path}", file=sys.stderr)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--sample", action="store_true", help="random (seeded) sample order")
    ap.add_argument("--two-pass", action="store_true",
                    help="add Stage-1b grounding critique (strips invented specifics)")
    ap.add_argument("--provider", choices=["grok", "gemini"], default="grok",
                    help="LLM provider (gemini = gemini-2.5-flash-lite, thinking off)")
    ap.add_argument("--out", default="processed.jsonl")
    args = ap.parse_args()
    configure_provider(args.provider)
    print(f"provider={args.provider} model={MODEL}", file=sys.stderr)
    if not args.all and not args.limit:
        args.limit = 20
    asyncio.run(main_async(args))
