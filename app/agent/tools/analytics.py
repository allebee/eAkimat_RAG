"""Module 2 Tools: Analytics — PostgreSQL query tools.

Uses mock data for demo, switches to real PostgreSQL when connected.
"""

from __future__ import annotations

import logging
from typing import Optional

from langchain_core.tools import tool

from app.config import settings

logger = logging.getLogger(__name__)


def _use_mock() -> bool:
    """Check if we should use mock data (no real PG connected)."""
    return not settings.postgres_dsn or settings.postgres_dsn == ""


@tool
def get_budget_amount(
    year: int,
    department_id: Optional[int] = None,
) -> str:
    """Get the total budget amount for a given year and optional department.

    Use this tool when the user asks about budget amounts, planned budgets,
    or budget allocations for a specific year or department.

    Args:
        year: The budget year (e.g., 2024, 2025).
        department_id: Optional department/ABP identifier.
    """
    if _use_mock():
        from app.agent.tools.mock_data import get_mock_budget
        return get_mock_budget(year, department_id)

    # Real implementation (activate when PG is connected)
    # from app.db.postgres import execute_query
    # sql = "SELECT SUM(amount) as total FROM budget_plan_data WHERE year = $1"
    # result = await execute_query(sql, {"year": year})
    return ""


@tool
def get_expenditure_fact(
    year: int,
    specifika: Optional[str] = None,
) -> str:
    """Get actual expenditure data for a given year.

    Use this tool when the user asks about actual spending, factual expenses,
    cash execution, or budget execution amounts.

    Args:
        year: The year to query.
        specifika: Optional budget specifika code.
    """
    if _use_mock():
        from app.agent.tools.mock_data import get_mock_expenditure
        return get_mock_expenditure(year)

    return ""


@tool
def get_income_plan(year: int) -> str:
    """Get the income plan data for a given year.

    Use this tool when the user asks about income, revenue,
    or receipt plans for a specific year.

    Args:
        year: The year to query.
    """
    if _use_mock():
        from app.agent.tools.mock_data import get_mock_income
        return get_mock_income(year)

    return ""


@tool
def get_kpi_status(
    month: str,
    employee_id: Optional[int] = None,
) -> str:
    """Get KPI status for a given month and optional employee.

    Use this tool when the user asks about KPI performance,
    indicators, or employee metrics.

    Args:
        month: Month in format 'YYYY-MM' (e.g., '2025-03').
        employee_id: Optional employee identifier.
    """
    return (
        f"⚠️ Модуль KPI ещё не подключён.\n"
        f"Запрос: KPI статус за {month}"
        + (f", сотрудник ID={employee_id}" if employee_id else "")
    )
