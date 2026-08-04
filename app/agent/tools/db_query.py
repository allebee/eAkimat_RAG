"""Module 2 Tool: PostgreSQL database query for budget analytics.

Three-step pipeline:
  1. Table Selection  — LLM picks relevant tables from a compact catalog
  2. Schema Loading   — exact column definitions loaded from db_schema_for_llm.md
  3. SQL Generation   — LLM generates SELECT with precise column names
"""

from __future__ import annotations

import asyncio
import logging
import re
from pathlib import Path
from typing import Dict, List, Optional

from langchain_core.tools import tool

from app.config import settings

logger = logging.getLogger(__name__)

# ── Paths ────────────────────────────────────────────────────────────────
SCHEMA_FILE = Path(__file__).resolve().parents[3] / "SQL" / "db_schema_for_llm.md"

# ── Compact table catalog for Step 1 (table selection) ───────────────────
# Groups the 987 tables into logical domains so the LLM can pick <5 tables
TABLE_CATALOG = """
ГРУППЫ ТАБЛИЦ eAkimat365 (database=postgres):

1. РАСХОДЫ БЮДЖЕТА:
   budget_cost_data — основная таблица расходов (value, year, region, gr, abp, prg, ppr, variant)
   budget_cost_correct — корректировки расходов
   budget_cost_data_sign — подписи к расходам
   budget_consolidate_calc_expens — консолидированные расходы ГУ (kass_ras, fact_ras, utoch_plan)

2. ДОХОДЫ БЮДЖЕТА:
   budget_income_data — доходная часть (kat, cls, pcl, spf, amount, year, region)
   budget_clarify_income — уточнения доходов
   budget_distribution_standard — нормативы распределения

3. ИСПОЛНЕНИЕ БЮДЖЕТА:
   budget_execution_alteration — корректировки исполнения (year, gu, spf, month, value)
   budget_execution_alteration_request — заявки на корректировку
   budget_execution_application9 — заявки приложение 9
   budget_execution_ipf_* — ИПФ (индивидуальный план финансирования)

4. БЮДЖЕТНЫЕ ЗАЯВКИ (формы расчётов):
   budget_request_form_01_* — формы расчетов по спецификам (111,112,113,121,131,etc)
   budget_request_form_gkkp_* — формы расчетов для ГККП

5. БИП (инвестиционные проекты):
   bip_agreement — согласования БИП (bip_code, abp, gu, status)
   bip_form_data — данные БИП проектов
   bip_criteria_values — критерии оценки
   bip_link_types — типы связей проектов

6. ШТАТНОЕ РАСПИСАНИЕ:
   staffing_table — основная таблица штатки (pos, full_name, region, retiree)
   stafftab_ead_d — данные ЕАД (штатных единиц)
   stafftab_report — отчёты по штатке
   stafftab_rep_val — значения отчётов

7. ДОГОВОРЫ И ПЛАТЕЖИ:
   budget_bc_agreement_registration — регистрация договоров
   budget_bc_payment_schedule — графики платежей (sum_payment, date_payment)
   budget_bc_payment_schedule_fact — фактические платежи

8. СПРАВОЧНИКИ:
   dict_gu — государственные учреждения (code, name_ru, id_region, gu_bin)
   dict_budget_regions — регионы
   dict_spf_* — специфики расходов
   dict_bp_* — бюджетные программы

9. ПРОГНОЗИРОВАНИЕ:
   forecast — прогнозы
   forecast_exec — прогнозы исполнения

10. МЕДИАМОНИТОРИНГ / СЭМ / СЭП:
    mb_bc — медиабюджетирование
    srs_form_data — формы СРС (потребности СНП)
"""


# ── SQL safety ───────────────────────────────────────────────────────────
WRITE_KEYWORDS = re.compile(
    r"\b(INSERT|UPDATE|DELETE|DROP|ALTER|CREATE|TRUNCATE|GRANT|REVOKE|EXEC)\b",
    re.IGNORECASE,
)


def _validate_sql(sql: str) -> tuple[bool, str]:
    """Validate SQL is read-only."""
    sql_clean = sql.strip().rstrip(";")
    if WRITE_KEYWORDS.search(sql_clean):
        return False, "Запрещено: только SELECT-запросы."
    if not sql_clean.upper().startswith("SELECT"):
        return False, "Запрос должен начинаться с SELECT."
    return True, ""


# ── Step 1: Table Selection ─────────────────────────────────────────────
def _select_tables(question: str) -> List[str]:
    """Use LLM to pick which tables are relevant for this question."""
    from langchain_openai import ChatOpenAI

    llm = ChatOpenAI(
        model=settings.llm_model,
        api_key=settings.llm_api_key,
        base_url=settings.llm_base_url,
        temperature=0,
        max_tokens=200,
    )

    prompt = f"""Ты аналитик базы данных eAkimat365.
Выбери от 1 до 5 таблиц, которые нужны для ответа на вопрос пользователя.
Верни ТОЛЬКО имена таблиц, по одному на строку, без пояснений.

{TABLE_CATALOG}

Вопрос: {question}

Таблицы:"""

    resp = llm.invoke(prompt)
    # Parse table names from response
    table_names = []
    for line in resp.content.strip().split("\n"):
        name = line.strip().strip("-").strip("•").strip()
        name = re.sub(r'\d+\.\s*', '', name).strip()  # remove "1. " prefix
        if name and re.match(r'^[a-z_]\w*$', name):
            table_names.append(name)
    
    logger.info("Step 1 — Selected tables: %s", table_names)
    return table_names[:5]


# ── Step 2: Schema Loading ──────────────────────────────────────────────
_schema_cache: Dict[str, str] = {}


def _load_schema_file() -> str:
    """Load and cache the full schema file."""
    if "full" not in _schema_cache:
        if SCHEMA_FILE.exists():
            _schema_cache["full"] = SCHEMA_FILE.read_text(encoding="utf-8")
            logger.info("Loaded schema file: %s (%d chars)", SCHEMA_FILE, len(_schema_cache["full"]))
        else:
            _schema_cache["full"] = ""
            logger.warning("Schema file not found: %s", SCHEMA_FILE)
    return _schema_cache["full"]


def _get_table_schema(table_names: List[str]) -> str:
    """Extract schema definitions for specific tables from the schema file."""
    full_schema = _load_schema_file()
    if not full_schema:
        return "Схема не найдена."

    schemas = []
    for table_name in table_names:
        # Pattern to match table section: ### Table: <name> ... until next ### or end
        pattern = rf"### Table: {re.escape(table_name)}\s*\n(.*?)(?=\n---|\Z)"
        match = re.search(pattern, full_schema, re.DOTALL)
        if match:
            schemas.append(f"### {table_name}\n{match.group(1).strip()}")
        else:
            # Try partial match for wildcard tables like budget_request_form_01_*
            schemas.append(f"### {table_name}\n(таблица не найдена в схеме — используй information_schema)")

    logger.info("Step 2 — Loaded schemas for %d/%d tables", 
                sum(1 for s in schemas if "не найдена" not in s), len(table_names))
    return "\n\n".join(schemas)


# ── Step 3: SQL Generation ──────────────────────────────────────────────
def _generate_sql(question: str, table_schemas: str) -> str:
    """Generate SQL using the exact column definitions."""
    from langchain_openai import ChatOpenAI

    llm = ChatOpenAI(
        model=settings.llm_model,
        api_key=settings.llm_api_key,
        base_url=settings.llm_base_url,
        temperature=0,
        max_tokens=500,
    )

    prompt = f"""Ты SQL-генератор для PostgreSQL базы eAkimat365.
Сгенерируй ТОЛЬКО один SQL-запрос (SELECT). Добавь LIMIT 20.
Используй ТОЛЬКО колонки из схемы ниже. НЕ придумывай колонки.

СХЕМА ТАБЛИЦ:
{table_schemas}

ВОПРОС: {question}

SQL:"""

    resp = llm.invoke(prompt)
    sql = resp.content.strip()
    sql = re.sub(r'^```(?:sql)?\s*', '', sql)
    sql = re.sub(r'\s*```$', '', sql)
    logger.info("Step 3 — Generated SQL: %s", sql.strip())
    return sql.strip()


# ── Main Tool ────────────────────────────────────────────────────────────
@tool
def query_database(
    question: str,
    sql_query: Optional[str] = None,
) -> str:
    """Query the eAkimat365 PostgreSQL database for budget analytics data.

    Use this tool when the user asks about specific numbers: budgets, plans,
    actual expenditures, income, staffing counts, BIP projects, or any
    quantitative / statistical data.

    DO NOT use this for procedural questions (how to fill forms, where to click).

    Available data domains:
    - budget_cost_data: расходы бюджета (value, year, region, gr, abp, prg)
    - budget_income_data: доходы бюджета (amount, year, region, kat, cls)
    - budget_consolidate_calc_expens: консолидированные расходы (kass_ras, fact_ras)
    - budget_execution_alteration: корректировки (year, gu, spf, month, value)
    - staffing_table: штатное расписание (pos, full_name, region)
    - dict_gu: справочник организаций (code, name_ru, id_region)
    - bip_agreement: БИП проекты (bip_code, status, region)
    - budget_bc_payment_schedule: графики платежей

    Args:
        question: The analytical question in natural language.
        sql_query: Optional pre-written SQL query (SELECT only).
    """
    dsn = settings.postgres_dsn

    # If SQL is pre-written, skip generation
    if sql_query:
        is_valid, error = _validate_sql(sql_query)
        if not is_valid:
            return f"❌ {error}"
    else:
        # 3-step pipeline: select tables → load schema → generate SQL
        try:
            # Step 1: Table selection
            tables = _select_tables(question)
            if not tables:
                return _mock_response(question)

            # Step 2: Load exact schema
            schema = _get_table_schema(tables)

            # Step 3: Generate SQL
            sql_query = _generate_sql(question, schema)
            is_valid, error = _validate_sql(sql_query)
            if not is_valid:
                return f"❌ {error}"
        except Exception as e:
            logger.warning("SQL pipeline failed: %s", e)
            return _mock_response(question)

    # Execute against real DB
    if dsn:
        try:
            import asyncpg

            # Use a direct connection (not pool) to avoid event loop conflicts
            async def _execute(sql, dsn_str):
                conn = await asyncpg.connect(dsn_str, timeout=10)
                try:
                    rows = await conn.fetch(sql)
                    return [dict(r) for r in rows]
                finally:
                    await conn.close()

            import concurrent.futures
            def _run(sql, dsn_str):
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                try:
                    return loop.run_until_complete(_execute(sql, dsn_str))
                finally:
                    loop.close()

            with concurrent.futures.ThreadPoolExecutor() as pool:
                result = pool.submit(_run, sql_query, dsn).result(timeout=15)

            if not result:
                return f"Запрос выполнен, данные не найдены.\n\nSQL: `{sql_query}`"

            return _format_results(result, sql_query)
        except Exception as e:
            logger.warning("DB query failed: %s", e)
            return f"❌ Ошибка выполнения запроса: {e}\n\nSQL: `{sql_query}`"

    return _mock_response(question)


# ── Result Formatting ────────────────────────────────────────────────────
def _format_results(rows: list, sql: str = "") -> str:
    """Format query results as a markdown table."""
    if not rows:
        return "Нет данных."

    columns = list(rows[0].keys())

    lines = []
    lines.append("| " + " | ".join(str(c) for c in columns) + " |")
    lines.append("|" + "|".join("---" for _ in columns) + "|")

    for row in rows[:50]:
        values = []
        for col in columns:
            val = row.get(col, "")
            if isinstance(val, float):
                val = f"{val:,.2f}".replace(",", " ")
            elif isinstance(val, int):
                val = f"{val:,}".replace(",", " ")
            values.append(str(val) if val is not None else "—")
        lines.append("| " + " | ".join(values) + " |")

    result = "\n".join(lines)
    if len(rows) > 50:
        result += f"\n\n... и ещё {len(rows) - 50} строк"

    return result


# ── Mock Fallback ────────────────────────────────────────────────────────
def _mock_response(question: str) -> str:
    """Generate mock responses when DB is unavailable."""
    q = question.lower()

    if any(w in q for w in ["бюджет", "план", "budget", "расход"]):
        return (
            "📊 Бюджетные данные (демо):\n"
            "| Год | Бюджет (тыс. тг) | Факт (тыс. тг) | % |\n"
            "|---|---|---|---|\n"
            "| 2023 | 38 500 000 | 36 200 000 | 94.0% |\n"
            "| 2024 | 45 230 000 | 42 100 000 | 88.0% |\n"
            "| 2025 | 52 100 000 | 12 800 000 | 24.6% |"
        )

    if any(w in q for w in ["доход", "income", "поступлен"]):
        return (
            "📊 Доходная часть (демо):\n"
            "| Источник | План (тыс. тг) | Факт (тыс. тг) |\n"
            "|---|---|---|\n"
            "| Налоговые | 32 000 000 | 30 500 000 |\n"
            "| Неналоговые | 5 200 000 | 4 800 000 |\n"
            "| Трансферты | 15 000 000 | 15 000 000 |"
        )

    if any(w in q for w in ["штат", "сотрудник", "staff"]):
        return (
            "📊 Штатное расписание (демо):\n"
            "| Категория | Утверждено | Факт | Вакансии |\n"
            "|---|---|---|---|\n"
            "| Руководители | 45 | 42 | 3 |\n"
            "| Специалисты | 230 | 218 | 12 |\n"
            "| **Итого** | **360** | **340** | **20** |"
        )

    if any(w in q for w in ["бип", "инвестиц", "проект"]):
        return (
            "📊 БИП проекты (демо):\n"
            "| Проект | Стоимость | Статус |\n"
            "|---|---|---|\n"
            "| Школа №45 | 2 500 000 | Реализация |\n"
            "| Дорога ул. Абая | 850 000 | Завершён |"
        )

    return (
        f"⚠️ Не удалось обработать запрос.\n"
        f"Вопрос: {question}"
    )
