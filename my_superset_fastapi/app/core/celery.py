from celery import Celery

from .config import get_settings

settings = get_settings()

celery_app = Celery("my_superset_fastapi", broker=settings.CELERY_BROKER_URL)
celery_app.conf.update(result_backend=settings.CELERY_RESULT_BACKEND)


@celery_app.task
def health_check() -> str:
    return "ok"


@celery_app.task(name="execute_sql")
def execute_sql(query_id: int) -> None:
    """Execute SQL in the background and store result."""
    from sqlalchemy import text
    from sqlalchemy.ext.asyncio import create_async_engine

    from app.core.db import AsyncSessionLocal
    from app.models import Database, QueryResult

    async def _run() -> None:
        async with AsyncSessionLocal() as session:
            result = await session.get(QueryResult, query_id)
            if not result:
                return
            db = await session.get(Database, result.database_id)
            engine = create_async_engine(db.sqlalchemy_uri)
            try:
                async with engine.connect() as conn:
                    res = await conn.execute(text(result.sql))
                    rows = res.fetchall()
                    result.result = str(rows)
                    result.rows = len(rows)
                    result.status = "success"
            except Exception as exc:  # noqa: BLE001
                result.status = "error"
                result.error = str(exc)
            finally:
                await engine.dispose()
                await session.commit()

    import asyncio

    asyncio.run(_run())
