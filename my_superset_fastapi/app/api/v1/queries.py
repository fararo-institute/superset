from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_db
from app.schemas.query import QueryCreate, QueryRead
from app.services.query_service import QueryService

router = APIRouter(prefix="/queries", tags=["queries"])

db_dep = Depends(get_db)


@router.post("/", response_model=QueryRead, status_code=status.HTTP_202_ACCEPTED)
async def submit_query(data: QueryCreate, db: AsyncSession = db_dep) -> QueryRead:
    result = await QueryService.submit_query(db, data.sql, data.database_id)
    return result


@router.get("/{query_id}", response_model=QueryRead)
async def get_query(query_id: int, db: AsyncSession = db_dep) -> QueryRead:
    result = await QueryService.get_result(db, query_id)
    if not result:
        raise HTTPException(status_code=404, detail="Query not found")
    return result
