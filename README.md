# eAkimat365 — Agentic RAG Service

Интеллектуальный помощник для системы бюджетного планирования eAkimat365 (Казахстан).  
Agentic RAG на базе **FastAPI + LangGraph + ChromaDB + GPT-4o**.

---

## Архитектура

Система состоит из 3 модулей:

| Модуль | Описание | Статус |
|--------|----------|--------|
| **Module 1 — База знаний** | Поиск по FAQ и PDF инструкциям через ChromaDB | ✅ Работает |
| **Module 2 — Аналитика** | SQL запросы к PostgreSQL (бюджет, расходы, доходы) | ⚠️ Демо-данные |
| **Module 3 — Навигация** | Контекстная фильтрация по текущей странице | ✅ Работает |

```
Пользователь → FastAPI → LangGraph Agent → [KB Tool / Analytics Tool] → Ответ
                  ↑                                      ↓
          X-Current-Context              ChromaDB / PostgreSQL
```

---

## Структура проекта

```
csi_rag/
├── app/                              # Основное приложение
│   ├── main.py                       # FastAPI app + lifespan
│   ├── config.py                     # Конфигурация (pydantic-settings)
│   │
│   ├── api/                          # API слой
│   │   ├── routes.py                 # /api/chat, /api/health, /api/ingest, /api/stats
│   │   └── schemas.py                # Pydantic модели запросов/ответов
│   │
│   ├── agent/                        # LangGraph агент
│   │   ├── graph.py                  # Граф агента (agent → tools → agent)
│   │   ├── prompts.py                # Системные промпты (RU/KK)
│   │   └── tools/                    # Инструменты агента
│   │       ├── knowledge_base.py     # Модуль 1: поиск по ChromaDB
│   │       ├── analytics.py          # Модуль 2: аналитика бюджета
│   │       └── mock_data.py          # Демо-данные для аналитики
│   │
│   ├── knowledge/                    # Хранилище знаний
│   │   ├── chromadb_store.py         # Singleton обёртка ChromaDB
│   │   └── context_mapping.py        # Модуль 3: page_id → фильтр
│   │
│   ├── ingestion/                    # Пайплайн загрузки данных
│   │   ├── deduplicator.py           # Дедупликация PDF (SHA256)
│   │   ├── pdf_loader.py             # Извлечение текста/изображений
│   │   ├── faq_loader.py             # Загрузка FAQ из Excel
│   │   └── instructions_loader.py    # Дерево навигации из Excel
│   │
│   └── db/                           # База данных
│       └── postgres.py               # Async PostgreSQL (asyncpg)
│
├── scripts/
│   └── ingest_all.py                 # CLI скрипт загрузки данных
│
├── tests/
│   ├── eval_dataset.json             # 18 тестовых кейсов
│   ├── eval_rag.py                   # Скрипт оценки RAG
│   └── eval_results.json             # Последние результаты
│
├── demo.html                         # Демо UI (чат)
├── Dockerfile                        # Контейнер
├── docker-compose.yml                # Docker Compose
├── requirements.txt                  # Зависимости
├── .env.example                      # Шаблон переменных окружения
└── .gitignore
```

### Данные (не в git)

```
├── pdf/                  # PDF инструкции (67 файлов)
├── prod_data/            # FAQ.xlsx, instructions.xlsx
├── chroma_data/          # ChromaDB persistence
├── storage/images/       # Извлечённые скриншоты из PDF
└── data/                 # navigation_tree.json
```

---

## Быстрый старт

### 1. Установка

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Конфигурация

```bash
cp .env.example .env
# Заполните OPENAI_API_KEY в .env
```

### 3. Загрузка данных

```bash
# Загрузить FAQ + PDF
python3 scripts/ingest_all.py --clear

# Только FAQ (быстро)
python3 scripts/ingest_all.py --faq-only

# Только PDF
python3 scripts/ingest_all.py --pdf-only
```

### 4. Запуск сервера

```bash
uvicorn app.main:app --port 8000

# Открыть демо UI
open http://localhost:8000
```

### 5. Оценка качества

```bash
# Полная оценка (с LLM)
python3 tests/eval_rag.py --verbose

# Только retrieval (бесплатно)
python3 tests/eval_rag.py --retrieval-only
```

---

## API

| Метод | Эндпоинт | Описание |
|-------|----------|----------|
| `GET` | `/` | Демо UI |
| `POST` | `/api/chat` | Чат с агентом |
| `GET` | `/api/health` | Статус системы |
| `POST` | `/api/ingest` | Загрузка данных |
| `GET` | `/api/stats` | Статистика ChromaDB |

### Пример запроса

```bash
curl -X POST http://localhost:8000/api/chat \
  -H "Content-Type: application/json" \
  -H "X-Current-Context: page_budget_staffing" \
  -d '{"message": "Как заполнить штатное расписание?", "language": "ru"}'
```

---

## Результаты оценки

| Метрика | Результат |
|---------|-----------|
| Hit Rate (top-5) | **92%** |
| MRR | **0.917** |
| Precision@5 | **86.7%** |
| Module Routing | **100%** |
| Keyword Hit Rate | **84%** |

---

## Docker

```bash
docker-compose up --build
```

---

## TODO

- [ ] Подключить PostgreSQL (Module 2)
- [ ] Получить реальные page_id от фронтенда (Module 3)
- [ ] Добавить ответы в FAQ Excel
- [ ] Поддержка казахского языка
