"""PostgreSQL connection manager (stubbed — waiting for analyst credentials)."""

from __future__ import annotations

import logging
from typing import Any, Dict, List, Optional

from app.config import settings

logger = logging.getLogger(__name__)

_pool = None


async def get_pool():
    """Get or create the async connection pool.

    TODO: Replace with asyncpg pool once credentials are available.
    """
    global _pool
    if _pool is not None:
        return _pool

    if not settings.postgres_dsn:
        raise ConnectionError("PostgreSQL DSN not configured. Set POSTGRES_DSN in .env")

    try:
        import asyncpg
        _pool = await asyncpg.create_pool(
            dsn=settings.postgres_dsn,
            min_size=2,
            max_size=10,
            command_timeout=10,
        )
        logger.info("PostgreSQL pool created")
        return _pool
    except Exception as exc:
        logger.error("Failed to connect to PostgreSQL: %s", exc)
        raise


async def execute_query(sql: str, params: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
    """Execute a read-only SQL query."""
    pool = await get_pool()
    async with pool.acquire() as conn:
        if params:
            rows = await conn.fetch(sql, *params.values())
        else:
            rows = await conn.fetch(sql)
        return [dict(row) for row in rows]


async def health_check() -> bool:
    """Check if PostgreSQL is reachable."""
    try:
        pool = await get_pool()
        async with pool.acquire() as conn:
            await conn.fetchval("SELECT 1")
        return True
    except Exception:
        return False


async def close_pool():
    """Close the connection pool on shutdown."""
    global _pool
    if _pool:
        await _pool.close()
        _pool = None
        logger.info("PostgreSQL pool closed")
