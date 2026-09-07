# eAkimat365 Agentic RAG — Project Context

> This document provides full context for any AI assistant working on this project.
> Last updated: 2026-04-29

## 1. What This Project Is

**eAkimat365** is Kazakhstan's government budget planning and execution system. This project is an **agentic RAG (Retrieval-Augmented Generation) chatbot** that helps government employees:

1. **Find instructions** — how to use the system (fill budget forms, approve requests, etc.)
2. **Query budget analytics** — real numbers from a production PostgreSQL database
3. **Navigate contextually** — answer questions relevant to the user's current page/module

The end users are **non-technical government analysts** who speak Russian and Kazakh.

---

## 2. Architecture Overview

```
┌──────────────┐      ┌──────────────────────────────┐
│  demo.html   │ ←──→ │  FastAPI (app/api/routes.py)  │
│  (frontend)  │      │  /api/chat  /api/chat/stream  │
└──────────────┘      └──────────────┬───────────────┘
                                     │
                      ┌──────────────▼───────────────┐
                      │  LangGraph Agent              │
                      │  (app/agent/graph.py)         │
                      │  2 tools, conditional routing  │
                      └──┬────────────────────────┬──┘
                         │                        │
              ┌──────────▼──────────┐  ┌──────────▼──────────┐
              │ search_knowledge_base│  │   query_database     │
              │ (ChromaDB vector    │  │ (3-step SQL pipeline) │
              │  search)            │  │                      │
              └──────────┬──────────┘  └──────────┬──────────┘
                         │                        │
              ┌──────────▼──────────┐  ┌──────────▼──────────┐
              │     ChromaDB        │  │    PostgreSQL        │
              │   2546 documents    │  │ 192.168.0.167:5432   │
              │  (PDF + video RAG)  │  │  database: postgres  │
              └─────────────────────┘  └─────────────────────┘
```

### LLM: xAI Grok
- Model: `grok-4-fast-non-reasoning` (via OpenAI-compatible API at `api.x.ai/v1`)
- Embeddings: OpenAI `text-embedding-3-small` (xAI has no embedding model)

### Agent: LangGraph
- File: `app/agent/graph.py`
- Flow: `agent → (tool calls?) → tools → agent → ... → END`
- The LLM decides which tool to call based on the question
- System prompt: `app/agent/prompts.py`

---

## 3. The Two Tools

### Tool 1: `search_knowledge_base` (ChromaDB)
- File: `app/agent/tools/knowledge_base.py`
- Searches 2546 chunks in ChromaDB (cosine similarity)
- Returns text + `[IMAGE: filename]` markers for inline screenshots
- Data sources:
  - **29 PDF instructions** from `pdf_instructions/` — budget forms, approval workflows
  - **47 video transcripts** from `video_instructions/` — screen recordings with extracted frames
  - Images stored in `storage/images/` (served via `/images/` endpoint)
- **Source-aware:** two buckets (instructional vs. support cases) are searched separately and
  merged under a quota, so call-center Q&A (~86% of the collection) cannot crowd out the official
  instructions and their screenshots.
- **Module-aware:** takes an optional `module` argument (the режим the user named, e.g. "Заявки ГУ").
  `app/knowledge/topics.py` maps it to a `topic` key, adds a targeted search over that module's
  official instructions, and re-scores candidates (match bonus / mismatch penalty). It never
  *filters* by topic — only `pdf_instruction` chunks use the controlled vocabulary, while video
  topics are free-form LLM labels (988 distinct) and call-center topics are coarse and often empty.
- Each returned chunk is prefixed with `[ИСТОЧНИК: ...]` so the agent knows whose interface wording
  is authoritative. The prompt forbids copying it; `routes.py` strips it as a backstop.

### Voice Input (Speech-to-Text)
- The frontend 🎤 mic button records voice and transcribes it to text, then **auto-sends**
  the question to the agent (ChatGPT voice-mode style).
- **Endpoint:** `POST /api/transcribe` (`app/api/routes.py`) — multipart `audio` file
  (webm/ogg/wav/mp3/...) → `{"text": "..."}`.
- **Engine:** `app/asr/engine.py` — 3iTech bilingual **RU+KK Wav2Vec2-CTC** TorchScript model
  (~720 MB), greedy CTC decode. Loaded lazily as a singleton on first request; inference
  runs in a threadpool (blocking, CPU-bound).
- **Model files:** `app/asr/model/{model.pt, tokens.lst, config.pbtxt}`. `model.pt` is
  **gitignored** (too large) — distribute separately and place it there.
- **Requires `ffmpeg`** on the host to decode browser webm/opus blobs (`brew install ffmpeg`).
- **Limitations:** acoustic model only — no punctuation/casing, no LM/beam-search; best on
  clean single-speaker speech.

### Tool 2: `query_database` (PostgreSQL — 3-step pipeline)
- File: `app/agent/tools/db_query.py`
- **Step 1 — Table Selection:** LLM picks 1-5 tables from a compact `TABLE_CATALOG` (10 domain groups)
- **Step 2 — Schema Loading:** Exact column definitions loaded from `SQL/db_schema_for_llm.md` (543KB, 987 tables)
- **Step 3 — SQL Generation:** LLM generates SELECT-only SQL with precise column names
- Execution: Direct `asyncpg.connect()` in a new event loop thread (avoids pool conflicts)
- Safety: Regex blocks all write operations (INSERT/UPDATE/DELETE/DROP/etc.)

---

## 4. Key Files Reference

```
csi_rag/
├── app/
│   ├── main.py                     # FastAPI app, startup, static file serving
│   ├── config.py                   # Pydantic settings from .env
│   ├── api/
│   │   ├── routes.py               # /chat, /chat/stream, /health, /ingest, /stats
│   │   └── schemas.py              # Pydantic request/response models
│   ├── agent/
│   │   ├── graph.py                # LangGraph agent (StateGraph with 2 tools)
│   │   ├── prompts.py              # System prompt (Modules 1-3 rules)
│   │   └── tools/
│   │       ├── knowledge_base.py   # Tool 1: ChromaDB search
│   │       └── db_query.py         # Tool 2: 3-step SQL pipeline
│   ├── db/
│   │   └── postgres.py             # asyncpg pool manager (used by health check)
│   ├── ingestion/
│   │   ├── pdf_loader.py           # PDF → chunks + [IMAGE:] markers
│   │   ├── video_rag_loader.py     # Video JSON → chunks + frame images
│   │   ├── instructions_loader.py  # Excel instructions loader
│   │   ├── faq_loader.py           # FAQ Excel loader
│   │   └── deduplicator.py         # PDF deduplication by hash
│   └── knowledge/
│       ├── chromadb_store.py        # ChromaDB wrapper (singleton)
│       └── context_mapping.py       # Page ID → label mapping
├── demo.html                        # Frontend (standalone, no framework)
├── scripts/
│   └── ingest_all.py               # CLI ingestion script
├── SQL/
│   ├── db_schema_for_llm.md        # Full DB schema (987 tables, from analyst)
│   └── db_schema_intgr_for_llm.md  # Integration schema (intgr)
├── pdf_instructions/                # 29 clean PDF files
├── video_instructions/              # 47 video transcripts + frames
├── storage/images/                  # Extracted images (served at /images/)
├── chroma_data/                     # ChromaDB persistent storage
├── .env                             # Secrets and config
└── requirements.txt                 # Python dependencies
```

---

## 5. Data Pipeline

### Ingestion (run via `scripts/ingest_all.py`)

```bash
# Full ingestion (clears existing data)
python scripts/ingest_all.py --clear

# Video only
python scripts/ingest_all.py --video-only

# PDF instructions only
python scripts/ingest_all.py --pdf-instructions-only
```

### PDF Processing (`app/ingestion/pdf_loader.py`)
- Extracts text + images per page using PyMuPDF (fitz)
- **Screenshot filtering — only ~32% of embedded images are real screenshots.** The rest are page
  header logos redrawn on every page (~40%) and tiny inline button glyphs (~28%). Three filters:
  an image whose xref appears on ≥ half the pages is a header/watermark; a rendered box smaller
  than 40×60pt is an inline glyph; under 2KB is a blank rectangle.
- **Layout-based image placement:** text blocks and surviving screenshots are sorted together by
  their coordinates on the page, so each `[IMAGE:]` marker lands exactly where the screenshot sits
  — after the step that introduces it, before its "Рис. X.Y" caption (verified: 86% of markers sit
  directly above a caption). Do **not** go back to pairing images with "Рис. X.Y" references by
  index: PDF resource order is not layout order, and headers/glyphs shift the pairing anyway —
  that was the cause of screenshots showing up under the wrong step.
- Chunks text at ~1500 chars with 200-char overlap

### Video Processing (`app/ingestion/video_rag_loader.py`)
- Reads `*_rag.json` files from `video_instructions/output_dataset/`
- Each JSON has: video name, transcript chunks, frame filenames
- Copies frame images to `storage/images/video/`
- Creates chunks with `[IMAGE: video/frame.jpg]` markers

### Image Rendering Pipeline
1. Ingestion stores `[IMAGE: filename]` markers in chunk text
2. ChromaDB search returns chunks with markers intact
3. LLM preserves markers in its response (system prompt enforces this)
4. `routes.py → _process_inline_images()` converts markers to `<img src="/images/..." />` HTML
5. Frontend renders inline screenshots

---

## 6. Frontend (`demo.html`)

- Standalone HTML file — no framework, no build step
- Premium dark theme with glassmorphism
- Features:
  - Context selector tabs (Бюджет, БИП, Штатка, etc.)
  - Quick action buttons (pre-filled queries)
  - SSE streaming via `/api/chat/stream`
  - Conversation history (in-memory, per session)
  - Custom markdown table parser → styled HTML tables (blue headers, striped rows)
  - Inline `<img>` rendering for screenshots
- Served by FastAPI's `StaticFiles` at `/demo.html`

---

## 7. PostgreSQL Database

- **Host:** `192.168.0.167:5432` (requires VPN to connect)
- **Database:** `postgres` (schema: `public`)
- **User:** `ai_agent_user` (SELECT-only) — password lives in `.env` (`POSTGRES_DSN`), not here
- **Tables:** 1069 in public schema, 987 documented in `SQL/db_schema_for_llm.md`
- **Key tables:**
  - `budget_cost_data` — 122K rows, main expenditure data
  - `budget_income_data` — 319K rows, revenue data
  - `budget_consolidate_calc_expens` — 25K rows, consolidated expenses
  - `staffing_table` — 10K rows, staffing
  - `dict_gu` — 44K rows, government organizations directory
  - `bip_agreement` — 5K rows, investment projects

### Important: TABLE_CATALOG needs improvement
The `TABLE_CATALOG` in `db_query.py` contains descriptions I inferred from table/column names. The analyst has NOT provided formal table descriptions yet. Ask for them if accuracy becomes an issue.

---

## 8. Decisions Made & Why

### Why Grok (not GPT-4)?
Customer requirement — the project specifically uses xAI's Grok API.

### Why direct `asyncpg.connect()` instead of connection pool?
The LangGraph tool runs in a ThreadPoolExecutor. Using the shared pool from `postgres.py` caused `"cannot perform operation: another operation is in progress"` and segfaults because the pool was created in a different event loop. Direct connections in a fresh event loop per query solved this.

### Why 3-step SQL pipeline (not just pass full schema)?
The schema file is 543KB (987 tables). That exceeds practical LLM context limits and causes hallucinated column names. The 3-step approach:
1. Select tables from a compact catalog (~2KB)
2. Load only those tables' exact columns from the schema file
3. Generate SQL with precise column definitions
This dramatically reduces hallucination.

### Why not use the `pdf/` folder?
The `pdf/` folder contains old duplicated PDFs. `pdf_instructions/` has 29 clean, renamed files provided by the analyst. Only `pdf_instructions/` is used in ingestion.

### Why filter screenshots by geometry, not by file size?
PDF extraction pulls out logos, watermarks, and inline button glyphs alongside real screenshots.
File size separates them badly: the header logos are 3-4KB, but 13% of genuine screenshots are also
under 15KB, so the old "skip < 15KB" rule silently dropped real screenshots while a per-page logo
still slipped through and consumed a step's image slot. Repetition across pages and rendered box
size identify the junk precisely, and that check now happens at ingestion (`pdf_loader.py`) where
the page geometry is available. `routes.py` keeps a 5KB backstop for chunks ingested before this.

### Why `[IMAGE:]` markers instead of base64?
Markers keep chunk sizes small in ChromaDB. Images are stored on disk and served via HTTP. The frontend renders them as `<img>` tags after server-side marker-to-HTML conversion.

---

## 9. Current Status & Known Issues

### ✅ Working
- Knowledge base search with inline screenshots (PDFs + videos)
- 3-step SQL analytics pipeline with live PostgreSQL
- Premium frontend with streaming, tables, and image rendering
- Multi-turn conversation (in-memory)

### ⚠️ Known Issues
- **🔴 PDF re-ingestion pending.** The screenshot-placement fix changes what ingestion writes, so
  chunks already in ChromaDB still carry the old, misaligned `[IMAGE:]` markers. Screenshots stay
  wrong until `python scripts/ingest_all.py --pdf-instructions-only` is re-run wherever the
  collection lives (the server — local embeddings are currently broken).
- **VPN required** for PostgreSQL — no graceful fallback message
- **No SQL retry** — if LLM generates bad SQL, the user sees the raw error
- **TABLE_CATALOG** descriptions are inferred, not from the analyst
- **Mock data fallback** still exists in db_query.py for when DB is unreachable

### 🧪 QA round 1 (report received 2026-09-01) — all four findings addressed
1. Assistant offered consolidation without asking the user's level → prompt now requires asking
   ГУ/АБП/УО **first** for level-gated actions (consolidation, свод, approval).
2. Screenshots attached to the wrong step → `pdf_loader.py` filters headers/glyphs and places
   images by page coordinates. **Needs re-ingestion to take effect.**
3. Answers drifted into a different режим (asked about Заявки ГУ, answered about Формы расчётов)
   → module-aware retrieval (`app/knowledge/topics.py`) + `module` tool argument the agent must
   carry across turns.
4. Invented eAkimat365 terminology → chunks are labelled by provenance and the prompt allows
   interface names only from official instructions, not from paraphrased support cases.

### 🔜 Planned / In Progress
- **dbt Gold Layer:** The analyst is building dbt views (Gold layer) over the raw tables. Once ready, replace `TABLE_CATALOG` + `db_schema_for_llm.md` with the Gold layer schema. This will be ~10-20 clean views instead of 987 raw tables, making SQL generation trivial.
- **Tech support call logs:** Audio recordings from 2023+ are available. Plan: transcribe with Whisper → ingest into ChromaDB → agent can reference real support cases when answering questions.

---

## 10. How to Run

```bash
# 1. Activate virtualenv
source venv/bin/activate

# 2. Start the server
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000

# 3. Open in browser
open http://localhost:8000

# 4. Re-ingest data (if needed)
python scripts/ingest_all.py --clear
```

### Environment Variables (`.env`)
```
GROK_API_KEY=...              # xAI Grok API key
GROK_MODEL=grok-4-fast-non-reasoning
GROK_BASE_URL=https://api.x.ai/v1
OPENAI_API_KEY=...            # For embeddings only
EMBEDDING_MODEL=text-embedding-3-small
CHROMA_PERSIST_DIR=./chroma_data
CHROMA_COLLECTION=eakimat365_knowledge
POSTGRES_DSN=postgresql://ai_agent_user:<password>@192.168.0.167:5432/postgres
STORAGE_DIR=./storage
```

---

## 11. Common Tasks

### Add new PDF instructions
1. Place PDFs in `pdf_instructions/`
2. Run `python scripts/ingest_all.py --pdf-instructions-only`

### Add new video transcripts
1. Place `*_rag.json` + frame images in `video_instructions/output_dataset/`
2. Run `python scripts/ingest_all.py --video-only`

### Update DB schema for dbt Gold layer
1. Replace `SQL/db_schema_for_llm.md` with new schema
2. Update `TABLE_CATALOG` in `app/agent/tools/db_query.py`
3. Restart the server

### Test analytics query
```bash
curl -s -X POST http://localhost:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"Сколько записей расходов за 2024 год?","language":"ru"}'
```

### Test knowledge base query
```bash
curl -s -X POST http://localhost:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"Как согласовать бюджетную заявку?","language":"ru"}'
```
