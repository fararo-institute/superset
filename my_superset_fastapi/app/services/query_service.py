from sqlalchemy.ext.asyncio import AsyncSession

from app.core.celery import celery_app
from app.models.query_result import QueryResult


class QueryService:
    @staticmethod
    async def submit_query(db: AsyncSession, sql: str, database_id: int) -> QueryResult:
        result = QueryResult(database_id=database_id, sql=sql)
        db.add(result)
        await db.commit()
        await db.refresh(result)
        celery_app.send_task("execute_sql", args=[result.id])
        return result

    @staticmethod
    async def get_result(db: AsyncSession, query_id: int) -> QueryResult | None:
        return await db.get(QueryResult, query_id)
