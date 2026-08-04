# eAkimat365 — Agentic RAG Service

Интеллектуальный помощник для системы бюджетного планирования **eAkimat365** (Казахстан).
Agentic RAG на базе **FastAPI + LangGraph + ChromaDB + xAI Grok**.

Пользователи — государственные аналитики. Бот отвечает на двух языках (RU / KK) и помогает:
1. найти инструкцию по работе с системой (PDF + видео-уроки);
2. получить аналитику из боевой PostgreSQL (бюджет, расходы, доходы, штатка, БИП);
3. ответить с учётом текущего модуля интерфейса (контекст страницы).

Поддерживается **голосовой ввод**: вопрос можно надиктовать — речь (RU/KK)
распознаётся локальной моделью и автоматически отправляется агенту.

---

## Архитектура

```
┌──────────────┐      ┌──────────────────────────────┐
│  demo.html   │ ←──→ │  FastAPI (app/api/routes.py) │
│  (frontend)  │      │  /api/chat  /api/chat/stream  │
│              │      │  /api/transcribe (STT)        │
└──────────────┘      └──────────────┬───────────────┘
                                     │
                      ┌──────────────▼──────────────┐
                      │      LangGraph Agent        │
                      │     (app/agent/graph.py)    │
                      └──┬───────────────────────┬──┘
                         │                       │
              ┌──────────▼──────────┐  ┌─────────▼──────────┐
              │ search_knowledge_   │  │   query_database    │
              │       base          │  │ (3-step SQL pipeline)│
              └──────────┬──────────┘  └──────────┬──────────┘
                         │                        │
              ┌──────────▼──────────┐  ┌──────────▼──────────┐
              │     ChromaDB        │  │    PostgreSQL        │
              │   ~2500 чанков      │  │ 192.168.0.167:5432   │
              │  (PDF + видео)      │  │ (SELECT-only user)   │
              └─────────────────────┘  └─────────────────────┘
```

**LLM:** xAI Grok (`grok-4-fast-non-reasoning`, OpenAI-совместимый API).
**Embeddings:** OpenAI `text-embedding-3-small` (у xAI нет embedding-модели).
**Vector store:** ChromaDB (persistent).
**SQL:** прямые подключения через `asyncpg` (без пула — изолированный event loop на каждый запрос).

---

## Структура проекта

```
csi_rag/
├── app/
│   ├── main.py                       # FastAPI app, lifespan, static /images/
│   ├── config.py                     # Pydantic settings (.env)
│   ├── api/
│   │   ├── routes.py                 # /api/chat, /api/chat/stream, /api/transcribe, /api/health, /api/stats
│   │   └── schemas.py                # Pydantic request/response модели
│   ├── asr/                          # Голосовой ввод (STT)
│   │   ├── engine.py                 # RU+KK Wav2Vec2-CTC движок (greedy decode)
│   │   └── model/                    # model.pt (~720 МБ, НЕ в git), tokens.lst, config.pbtxt
│   ├── agent/
│   │   ├── graph.py                  # LangGraph (agent ↔ tools)
│   │   ├── prompts.py                # Системный промпт (RU/KK)
│   │   └── tools/
│   │       ├── knowledge_base.py     # Tool 1: поиск по ChromaDB
│   │       └── db_query.py           # Tool 2: 3-шаговый SQL pipeline
│   ├── knowledge/
│   │   ├── chromadb_store.py         # Singleton-обёртка ChromaDB
│   │   └── context_mapping.py        # page_id → фильтр модуля
│   ├── ingestion/
│   │   ├── pdf_loader.py             # PDF → чанки + [IMAGE:] маркеры
│   │   ├── video_rag_loader.py       # Видео-транскрипты → чанки + кадры
│   │   ├── call_loader.py            # Whisper-транскрипты звонков поддержки
│   │   ├── instructions_loader.py    # Excel-инструкции (legacy)
│   │   ├── faq_loader.py             # FAQ Excel (legacy)
│   │   └── deduplicator.py           # SHA256-дедуп PDF
│   └── db/
│       └── postgres.py               # asyncpg pool (используется только в /health)
│
├── scripts/
│   └── ingest_all.py                 # CLI ingestion (--clear, --pdf-only, --video-only …)
│
├── SQL/
│   ├── db_schema_for_llm.md          # Полная схема (987 таблиц, 532 КБ)
│   └── db_schema_intgr_for_llm.md    # Схема intgr-слоя
│
├── demo.html                          # Frontend (без фреймворка, SSE-стриминг)
├── Dockerfile / docker-compose.yml
├── requirements.txt
├── .env.example
└── CLAUDE.md                          # Полный контекст проекта для AI-ассистентов
```

### Не в git (нужно перенести на сервер отдельно)

```
pdf_instructions/      # 29 PDF (источник для ingestion)         ~42 МБ
video_instructions/    # JSON-транскрипты + кадры                ~1.9 ГБ
MP3toTXT/              # Whisper-транскрипты звонков             ~0.9 МБ
chroma_data/           # ChromaDB persistence (готовый индекс)   ~130 МБ
storage/images/        # Скриншоты из PDF и кадры из видео       ~340 МБ
app/asr/model/model.pt # ASR-модель для голосового ввода (STT)   ~720 МБ
.env                   # Секреты
```

---

## Два инструмента агента

### Tool 1 — `search_knowledge_base` (ChromaDB)
`app/agent/tools/knowledge_base.py`. Cosine-similarity поиск по чанкам. Возвращает текст с маркерами `[IMAGE: filename]`, которые `routes.py` превращает в `<img src="/images/...">`. Источники: 29 PDF и ~47 видео-уроков.

### Tool 2 — `query_database` (PostgreSQL, 3 шага)
`app/agent/tools/db_query.py`.
1. **Выбор таблиц** — LLM выбирает 1–5 таблиц из компактного `TABLE_CATALOG` (~2 КБ).
2. **Загрузка схемы** — точные определения колонок берутся из `SQL/db_schema_for_llm.md`.
3. **Генерация SQL** — только `SELECT`. Регулярка блокирует `INSERT/UPDATE/DELETE/DROP/...`.

Выполнение: новый event loop в отдельном потоке + `asyncpg.connect()` (не пул).
Причина: LangGraph-инструмент работает в `ThreadPoolExecutor`, и shared-пул в чужом event loop ломается с `another operation is in progress`.

---

## Голосовой ввод (Speech-to-Text)

Кнопка 🎤 в `demo.html` записывает речь через `MediaRecorder`, отправляет аудио на
`/api/transcribe`, а распознанный текст вставляется в поле ввода и **сразу отправляется**
агенту (как голосовой режим ChatGPT).

**Эндпоинт:** `POST /api/transcribe` — `multipart/form-data` с полем `audio`
(webm/ogg/wav/mp3/m4a/…), ответ `{"text": "распознанный текст"}`.

```bash
curl -s -X POST http://localhost:8000/api/transcribe -F "audio=@запись.wav"
# -> {"text":"как заполнить штатное расписание"}
```

**Движок:** `app/asr/engine.py` — двуязычная (RU+KK) Wav2Vec2-CTC модель (3iTech,
TorchScript, greedy CTC). Грузится лениво синглтоном на первый запрос (~720 МБ в память);
инференс выполняется в threadpool (блокирующий, CPU-bound). Лимит загрузки — 25 МБ.

- **Файлы модели:** `app/asr/model/{model.pt, tokens.lst, config.pbtxt}`. `model.pt` (~720 МБ)
  **не в git** — переносится на сервер отдельно (см. раздел «Деплой»).
- **Нужен `ffmpeg`** на хосте — для декодирования браузерного webm/opus
  (`brew install ffmpeg` / `apt install ffmpeg`).
- **Ограничения:** только акустическая модель — без пунктуации и заглавных букв,
  без языковой модели/beam-search; качество выше всего на чистой одноголосой речи.

---

## Локальный запуск

```bash
# 1. venv + зависимости
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 2. конфиг
cp .env.example .env
# заполнить ключи (см. ниже)

# 3. запуск
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000

# 4. UI
open http://localhost:8000
```

### Переменные окружения (`.env`)

```dotenv
GROK_API_KEY=...
GROK_MODEL=grok-4-fast-non-reasoning
GROK_BASE_URL=https://api.x.ai/v1

OPENAI_API_KEY=...                # только для эмбеддингов
EMBEDDING_MODEL=text-embedding-3-small

CHROMA_PERSIST_DIR=./chroma_data
CHROMA_COLLECTION=eakimat365_knowledge

POSTGRES_DSN=postgresql://ai_agent_user:<password>@192.168.0.167:5432/postgres

STORAGE_DIR=./storage
```

> PostgreSQL доступен **только из VPN**. Без VPN Tool 2 будет падать с ошибкой подключения.

---

## Ingestion

```bash
# Полная перезаливка (очищает коллекцию)
python scripts/ingest_all.py --clear

# Только PDF из pdf_instructions/
python scripts/ingest_all.py --pdf-instructions-only

# Только видео из video_instructions/output_dataset/
python scripts/ingest_all.py --video-only

# Только звонки поддержки из MP3toTXT/
python scripts/ingest_all.py --calls-only
```

После ingestion в `chroma_data/` появляется индекс, в `storage/images/` — изображения. Эти две папки и нужны рантайму.

---

## API

| Метод | Эндпоинт          | Описание                              |
|-------|-------------------|---------------------------------------|
| GET   | `/`               | Демо UI                               |
| POST  | `/api/chat`       | Синхронный чат                        |
| POST  | `/api/chat/stream`| SSE-стриминг                          |
| GET   | `/api/health`     | Статус ChromaDB + PostgreSQL          |
| POST  | `/api/ingest`     | Запуск ingestion из HTTP              |
| GET   | `/api/stats`      | Кол-во документов в ChromaDB          |
| GET   | `/images/...`     | Раздача `storage/images/`             |

### Примеры

```bash
# Поиск по базе знаний
curl -s -X POST http://localhost:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"Как согласовать бюджетную заявку?","language":"ru"}'

# Аналитика (нужен VPN)
curl -s -X POST http://localhost:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"Сколько записей расходов за 2024 год?","language":"ru"}'
```

---

## Деплой на сервер

Репозиторий не содержит данные (vector DB, изображения, исходные PDF/видео) — они тяжёлые и переносятся отдельно.

### 1. Код

```bash
git clone https://github.com/allebee/eAkimat_RAG.git
cd eAkimat_RAG
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # заполнить ключи

# ffmpeg нужен для голосового ввода (декодирование webm/opus из браузера)
sudo apt install -y ffmpeg     # Debian/Ubuntu  (macOS: brew install ffmpeg)
```

### 2. Данные (выбрать один из вариантов)

**Вариант A — перенести готовый индекс (быстро, без эмбеддингов).**
С локальной машины:
```bash
rsync -avz --progress chroma_data/ user@server:/path/to/eAkimat_RAG/chroma_data/
rsync -avz --progress storage/      user@server:/path/to/eAkimat_RAG/storage/
# ASR-модель для голосового ввода (~720 МБ, не в git):
rsync -avz --progress app/asr/model/model.pt user@server:/path/to/eAkimat_RAG/app/asr/model/model.pt
```

**Вариант B — переингестить на сервере (меньше трафика).**
Перенести только источники и пересобрать индекс:
```bash
rsync -avz pdf_instructions/ user@server:/path/to/eAkimat_RAG/pdf_instructions/
# опционально:
rsync -avz video_instructions/ user@server:/path/to/eAkimat_RAG/video_instructions/
# на сервере:
python scripts/ingest_all.py --clear
```

### 3. Запуск

```bash
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Для прод-режима рекомендуется обернуть в systemd / supervisor / docker-compose и поставить за reverse proxy (nginx) с TLS.

### Docker

```bash
docker-compose up --build
```

`chroma_data/` и `storage/` пробрасываются как volumes — наполнить их нужно одним из способов выше до запуска.

---

## Известные ограничения

- **VPN обязателен** для Tool 2 (PostgreSQL во внутренней сети).
- **Нет ретрая SQL** — если LLM сгенерировал невалидный запрос, пользователь видит сырую ошибку.
- **`TABLE_CATALOG`** в `db_query.py` собран по именам колонок, описаний от аналитика пока нет.
- **История диалога** — в памяти процесса; перезапуск всё стирает.

## В планах

- **dbt Gold layer:** заменить `TABLE_CATALOG` + сырую схему на ~10–20 чистых витрин.
- **Звонки поддержки:** Whisper-транскрипты 2023+ в ChromaDB как ещё один источник.
- **Персистентная история** диалогов.

---

См. также [CLAUDE.md](CLAUDE.md) — полный контекст проекта для AI-ассистентов.
