from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_db
from app.schemas.database import DatabaseCreate, DatabaseRead
from app.services.database_service import DatabaseService

router = APIRouter(prefix="/databases", tags=["databases"])


@router.post("/", response_model=DatabaseRead, status_code=status.HTTP_201_CREATED)
async def create_database(
    data: DatabaseCreate,
    db: AsyncSession = Depends(get_db),  # noqa: B008
) -> DatabaseRead:
    return await DatabaseService.create(db, data)


@router.post("/test", status_code=status.HTTP_200_OK)
async def test_connection(
    data: DatabaseCreate,
    db: AsyncSession = Depends(get_db),  # noqa: B008,PT028
) -> dict[str, str]:
    await DatabaseService.test_connection(data)
    return {"status": "ok"}


@router.get("/{database_id}/schema", status_code=status.HTTP_200_OK)
async def get_schema(
    database_id: int,
    db: AsyncSession = Depends(get_db),  # noqa: B008
) -> dict[str, list[str]]:
    return await DatabaseService.introspect_schema(db, database_id)
