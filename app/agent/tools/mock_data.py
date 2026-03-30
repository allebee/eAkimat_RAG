"""Mock analytics data for demo purposes.

Provides realistic budget data so Module 2 can be demonstrated
before we receive actual PostgreSQL access.
"""

from __future__ import annotations

# Realistic mock data based on Kazakhstan budget structures
MOCK_BUDGET_DATA = {
    2023: {
        "total": 285_400_000_000,
        "departments": {
            1: {"name": "Управление образования", "amount": 45_200_000_000},
            2: {"name": "Управление здравоохранения", "amount": 38_700_000_000},
            3: {"name": "Управление строительства", "amount": 52_100_000_000},
            4: {"name": "Управление культуры", "amount": 12_300_000_000},
            5: {"name": "Управление сельского хозяйства", "amount": 28_500_000_000},
        },
    },
    2024: {
        "total": 312_800_000_000,
        "departments": {
            1: {"name": "Управление образования", "amount": 49_800_000_000},
            2: {"name": "Управление здравоохранения", "amount": 42_100_000_000},
            3: {"name": "Управление строительства", "amount": 57_600_000_000},
            4: {"name": "Управление культуры", "amount": 13_500_000_000},
            5: {"name": "Управление сельского хозяйства", "amount": 31_200_000_000},
        },
    },
    2025: {
        "total": 341_500_000_000,
        "departments": {
            1: {"name": "Управление образования", "amount": 54_200_000_000},
            2: {"name": "Управление здравоохранения", "amount": 46_800_000_000},
            3: {"name": "Управление строительства", "amount": 62_300_000_000},
            4: {"name": "Управление культуры", "amount": 14_800_000_000},
            5: {"name": "Управление сельского хозяйства", "amount": 34_100_000_000},
        },
    },
}

MOCK_EXPENDITURE_FACT = {
    2023: {"plan": 285_400_000_000, "fact": 271_130_000_000, "execution_pct": 95.0},
    2024: {"plan": 312_800_000_000, "fact": 297_160_000_000, "execution_pct": 95.0},
    2025: {"plan": 341_500_000_000, "fact": 187_825_000_000, "execution_pct": 55.0},
}

MOCK_INCOME_PLAN = {
    2023: {"plan": 298_200_000_000, "fact": 305_100_000_000},
    2024: {"plan": 325_400_000_000, "fact": 331_700_000_000},
    2025: {"plan": 355_800_000_000, "fact": None},
}


def format_money(amount: int) -> str:
    """Format amount in tenge with space thousands separator."""
    return f"{amount:,.0f}".replace(",", " ") + " тг"


def get_mock_budget(year: int, department_id: int | None = None) -> str:
    """Get mock budget data."""
    data = MOCK_BUDGET_DATA.get(year)
    if not data:
        return f"Данные за {year} год отсутствуют в демо-режиме."

    if department_id:
        dept = data["departments"].get(department_id)
        if dept:
            return (
                f"Бюджет {dept['name']} на {year} год: "
                f"{format_money(dept['amount'])}"
            )
        return f"Подразделение с ID={department_id} не найдено."

    # All departments summary
    lines = [f"Общий бюджет на {year} год: {format_money(data['total'])}", ""]
    lines.append("По подразделениям:")
    for did, dept in data["departments"].items():
        lines.append(f"  • {dept['name']}: {format_money(dept['amount'])}")
    return "\n".join(lines)


def get_mock_expenditure(year: int) -> str:
    """Get mock expenditure fact data."""
    data = MOCK_EXPENDITURE_FACT.get(year)
    if not data:
        return f"Данные по расходам за {year} год отсутствуют в демо-режиме."

    lines = [
        f"Исполнение бюджета за {year} год:",
        f"  • План: {format_money(data['plan'])}",
        f"  • Факт: {format_money(data['fact'])}",
        f"  • Исполнение: {data['execution_pct']}%",
    ]
    return "\n".join(lines)


def get_mock_income(year: int) -> str:
    """Get mock income plan data."""
    data = MOCK_INCOME_PLAN.get(year)
    if not data:
        return f"Данные по доходам за {year} год отсутствуют в демо-режиме."

    lines = [
        f"Доходная часть бюджета за {year} год:",
        f"  • План: {format_money(data['plan'])}",
    ]
    if data["fact"]:
        lines.append(f"  • Факт: {format_money(data['fact'])}")
    else:
        lines.append("  • Факт: данные ещё не поступили")
    return "\n".join(lines)
