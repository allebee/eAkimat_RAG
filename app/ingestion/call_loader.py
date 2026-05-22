"""Support-call transcript loader.

Reads Whisper-transcribed support calls from MP3toTXT/, cleans hallucinated
subtitle artifacts, uses Grok to extract a structured Q&A summary per call,
and emits ChromaDB documents.

Filename convention (one file per call):
    YYYY-MM-DD_HH-MM_<caller_phone>_<call_id>.txt

Each call produces up to two ChromaDB documents:
  1. summary chunk  — Grok-extracted problem + step-by-step solution
                      (primary retrieval target)
  2. transcript chunk — cleaned raw transcript (secondary, for verbatim quotes)

Both chunks share `call_id` in metadata so the agent can cross-reference.
LLM cleaning output is cached per call_id to make re-runs free.
"""

from __future__ import annotations

import hashlib
import json
import logging
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional

from openai import OpenAI

from app.config import settings

logger = logging.getLogger(__name__)

# Minimum raw transcript size (bytes) — smaller files are dial tones / hangups.
MIN_FILE_BYTES = 500

# Minimum cleaned text length to keep a chunk.
MIN_CHUNK_LENGTH = 80

# Filename pattern: 2026-04-20_15-48_77058160564_6530275773.txt
FILENAME_RE = re.compile(
    r"^(?P<date>\d{4}-\d{2}-\d{2})_"
    r"(?P<time>\d{2}-\d{2})_"
    r"(?P<phone>\d+)_"
    r"(?P<call_id>\d+)\.txt$"
)

# Timestamp line: [12.34 - 56.78]
TIMESTAMP_RE = re.compile(r"^\[\s*([\d.]+)\s*-\s*([\d.]+)\s*\]\s*$")

# Whisper hallucination patterns (YouTube subtitle training-data leakage).
# Any line matching these is dropped entirely.
HALLUCINATION_PATTERNS = [
    re.compile(r"DimaTorzok", re.I),
    re.compile(r"Субтитры (?:сделал|создавал|подогнал)", re.I),
    re.compile(r"Редактор субтитров", re.I),
    re.compile(r"Корректор\s+[А-ЯA-Z]\.", re.I),
    re.compile(r"^Спасибо за просмотр\.?$", re.I),
    re.compile(r"^Продолжение следует\.{0,3}$", re.I),
    re.compile(r"^Симон\s*$", re.I),
]


@dataclass
class CallSegment:
    """One timestamped segment from a Whisper transcript."""
    start: float
    end: float
    text: str


@dataclass
class ParsedCall:
    """A parsed transcript file before LLM cleaning."""
    call_id: str
    caller_phone: str
    date: str            # YYYY-MM-DD
    time: str            # HH-MM
    duration_sec: float
    segments: List[CallSegment]
    clean_transcript: str  # segments joined, hallucinations stripped


# ---------------------------------------------------------------------------
# Parsing
# ---------------------------------------------------------------------------

def _is_hallucination(line: str) -> bool:
    return any(p.search(line) for p in HALLUCINATION_PATTERNS)


def _parse_transcript(path: Path) -> Optional[ParsedCall]:
    """Parse a single transcript file. Returns None if the file is unusable."""
    m = FILENAME_RE.match(path.name)
    if not m:
        logger.debug("Skipping non-matching filename: %s", path.name)
        return None

    try:
        raw = path.read_text(encoding="utf-8")
    except OSError as e:
        logger.warning("Failed to read %s: %s", path, e)
        return None

    if len(raw.encode("utf-8")) < MIN_FILE_BYTES:
        logger.debug("Skipping tiny file (<%dB): %s", MIN_FILE_BYTES, path.name)
        return None

    segments: List[CallSegment] = []
    current_start: Optional[float] = None
    current_end: Optional[float] = None
    current_text_parts: List[str] = []

    def _flush():
        if current_start is None or not current_text_parts:
            return
        text = " ".join(t.strip() for t in current_text_parts if t.strip())
        if text and not _is_hallucination(text):
            segments.append(CallSegment(
                start=current_start,
                end=current_end if current_end is not None else current_start,
                text=text,
            ))

    for line in raw.splitlines():
        line = line.rstrip()
        if not line:
            continue
        ts = TIMESTAMP_RE.match(line)
        if ts:
            _flush()
            current_start = float(ts.group(1))
            current_end = float(ts.group(2))
            current_text_parts = []
        else:
            if _is_hallucination(line):
                continue
            current_text_parts.append(line)
    _flush()

    if not segments:
        logger.debug("No usable segments after cleaning: %s", path.name)
        return None

    clean_text = "\n".join(s.text for s in segments)
    if len(clean_text) < MIN_CHUNK_LENGTH:
        logger.debug("Cleaned transcript too short: %s", path.name)
        return None

    return ParsedCall(
        call_id=m.group("call_id"),
        caller_phone=m.group("phone"),
        date=m.group("date"),
        time=m.group("time"),
        duration_sec=segments[-1].end,
        segments=segments,
        clean_transcript=clean_text,
    )


# ---------------------------------------------------------------------------
# LLM cleaning (Grok)
# ---------------------------------------------------------------------------

_GROK_CLIENT: Optional[OpenAI] = None


def _grok_client() -> OpenAI:
    global _GROK_CLIENT
    if _GROK_CLIENT is None:
        _GROK_CLIENT = OpenAI(
            api_key=settings.grok_api_key,
            base_url=settings.grok_base_url,
        )
    return _GROK_CLIENT


SUMMARY_PROMPT = """Ты обрабатываешь стенограмму телефонного звонка в техподдержку системы eAkimat365 (бюджетное планирование Казахстана).

Стенограмма содержит реплики оператора и пользователя БЕЗ разделения по говорящим, может быть на русском и казахском, иногда с ошибками распознавания речи.

Извлеки из неё структурированный конспект для базы знаний. Верни СТРОГО JSON без markdown-обёрток:

{
  "skip": false,
  "skip_reason": "",
  "problem": "Краткая формулировка проблемы пользователя (1-2 предложения, на русском)",
  "solution_steps": ["Шаг 1...", "Шаг 2...", "..."],
  "modules": ["Штатка", "Бюджет", ...],
  "forms_specifika": ["112", "0.29", "149", "..."],
  "summary": "Развернутое описание кейса 3-5 предложений, как могло бы быть в FAQ. На русском."
}

Правила:
- Если в звонке НЕТ внятной проблемы и решения (приветствие, набор цифр, тестовый звонок, обрыв) — верни {"skip": true, "skip_reason": "..."}.
- modules — выбирай из: Штатка, Бюджет, БИП, Доходы, Расходы, Налоги, Согласование, Другое.
- forms_specifika — упомянутые в разговоре номера форм, спецификов, программ (например "112", "0.29", "149", "ЕР1А6").
- НЕ выдумывай факты, которых нет в стенограмме.
- Пиши на русском, даже если в стенограмме есть казахские фрагменты.

Стенограмма:
---
{transcript}
---
"""


def _llm_summarize(transcript: str) -> Optional[Dict[str, Any]]:
    """Call Grok to extract structured summary. Returns None on failure."""
    client = _grok_client()
    try:
        resp = client.chat.completions.create(
            model=settings.grok_model,
            messages=[
                {"role": "user", "content": SUMMARY_PROMPT.replace("{transcript}", transcript)},
            ],
            temperature=0.1,
            response_format={"type": "json_object"},
        )
        content = resp.choices[0].message.content or ""
        return json.loads(content)
    except json.JSONDecodeError as e:
        logger.warning("Grok returned invalid JSON: %s", e)
        return None
    except Exception as e:
        logger.warning("Grok call failed: %s", e)
        return None


def _load_cached_summary(cache_dir: Path, call_id: str) -> Optional[Dict[str, Any]]:
    cache_file = cache_dir / f"{call_id}.json"
    if not cache_file.exists():
        return None
    try:
        return json.loads(cache_file.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return None


def _save_cached_summary(cache_dir: Path, call_id: str, summary: Dict[str, Any]) -> None:
    cache_dir.mkdir(parents=True, exist_ok=True)
    cache_file = cache_dir / f"{call_id}.json"
    try:
        cache_file.write_text(
            json.dumps(summary, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
    except OSError as e:
        logger.warning("Failed to cache summary for %s: %s", call_id, e)


# ---------------------------------------------------------------------------
# Document construction
# ---------------------------------------------------------------------------

def _doc_id(prefix: str, call_id: str) -> str:
    raw = f"{prefix}_{call_id}"
    return f"call_{prefix}_{hashlib.md5(raw.encode()).hexdigest()}"


def _build_documents(call: ParsedCall, summary: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Build 1-2 ChromaDB documents from a parsed call + LLM summary."""
    if summary.get("skip"):
        logger.debug("Skipping call %s: %s", call.call_id, summary.get("skip_reason"))
        return []

    problem = (summary.get("problem") or "").strip()
    steps = summary.get("solution_steps") or []
    modules = summary.get("modules") or []
    forms = summary.get("forms_specifika") or []
    full_summary = (summary.get("summary") or "").strip()

    if not problem or not steps:
        logger.debug("Call %s missing problem/steps — skipping", call.call_id)
        return []

    # --- Summary chunk (primary retrieval target) -------------------------
    steps_block = "\n".join(f"{i}. {s}" for i, s in enumerate(steps, 1))
    summary_text = (
        f"Реальный кейс из техподдержки eAkimat365 (звонок от {call.date}).\n\n"
        f"**Проблема пользователя:** {problem}\n\n"
        f"**Решение:**\n{steps_block}\n\n"
        f"**Описание:** {full_summary}"
    )

    base_meta: Dict[str, Any] = {
        "source_type": "support_call",
        "call_id": call.call_id,
        "date": call.date,
        "time": call.time,
        "caller_phone": call.caller_phone,
        "duration_sec": round(call.duration_sec, 1),
        # ChromaDB metadata can't hold lists — store as comma-joined strings.
        "modules": ", ".join(modules),
        "forms_specifika": ", ".join(forms),
    }

    documents: List[Dict[str, Any]] = [{
        "id": _doc_id("summary", call.call_id),
        "content": summary_text,
        "metadata": {**base_meta, "chunk_kind": "summary"},
    }]

    # --- Raw transcript chunk (secondary, for verbatim quotes) ------------
    transcript_text = (
        f"Стенограмма звонка в техподдержку от {call.date} "
        f"(тема: {problem}).\n\n{call.clean_transcript}"
    )
    documents.append({
        "id": _doc_id("transcript", call.call_id),
        "content": transcript_text,
        "metadata": {**base_meta, "chunk_kind": "transcript"},
    })

    return documents


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def load_all_calls(
    calls_dir: str,
    use_llm: bool = True,
    cache_subdir: str = ".cache",
) -> List[Dict[str, Any]]:
    """Load and process all transcript files in ``calls_dir``.

    Args:
        calls_dir: Path to the MP3toTXT directory.
        use_llm: If True, run Grok cleaning (with per-call cache).
                 If False, emit only raw transcript chunks (debug mode).
        cache_subdir: Subdirectory under calls_dir for LLM summary cache.

    Returns:
        List of ChromaDB documents.
    """
    root = Path(calls_dir)
    if not root.exists():
        logger.warning("Calls directory not found: %s", root)
        return []

    cache_dir = root / cache_subdir

    files = sorted(p for p in root.iterdir() if p.is_file() and p.suffix == ".txt")
    logger.info("Found %d transcript files in %s", len(files), root)

    all_docs: List[Dict[str, Any]] = []
    n_parsed = n_skipped_parse = n_skipped_llm = n_cached = n_llm_called = 0

    for path in files:
        call = _parse_transcript(path)
        if call is None:
            n_skipped_parse += 1
            continue
        n_parsed += 1

        if not use_llm:
            # Raw-only mode: emit a single transcript chunk with no summary.
            doc_id = _doc_id("raw", call.call_id)
            all_docs.append({
                "id": doc_id,
                "content": (
                    f"Стенограмма звонка в техподдержку от {call.date}.\n\n"
                    f"{call.clean_transcript}"
                ),
                "metadata": {
                    "source_type": "support_call",
                    "call_id": call.call_id,
                    "date": call.date,
                    "time": call.time,
                    "caller_phone": call.caller_phone,
                    "duration_sec": round(call.duration_sec, 1),
                    "chunk_kind": "transcript_raw",
                },
            })
            continue

        summary = _load_cached_summary(cache_dir, call.call_id)
        if summary is not None:
            n_cached += 1
        else:
            logger.info("LLM summarizing call %s (%s)...", call.call_id, path.name)
            summary = _llm_summarize(call.clean_transcript)
            n_llm_called += 1
            if summary is None:
                n_skipped_llm += 1
                continue
            _save_cached_summary(cache_dir, call.call_id, summary)

        docs = _build_documents(call, summary)
        if not docs:
            n_skipped_llm += 1
            continue
        all_docs.extend(docs)

    logger.info(
        "Calls: parsed=%d  skipped_parse=%d  cached=%d  llm_called=%d  "
        "skipped_after_llm=%d  → %d documents",
        n_parsed, n_skipped_parse, n_cached, n_llm_called, n_skipped_llm, len(all_docs),
    )
    return all_docs
