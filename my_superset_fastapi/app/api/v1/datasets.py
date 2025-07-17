from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_db
from app.schemas.dataset import DatasetCreate, DatasetRead
from app.services.dataset_service import DatasetService

router = APIRouter(prefix="/datasets", tags=["datasets"])


@router.post("/", response_model=DatasetRead, status_code=status.HTTP_201_CREATED)
async def create_dataset(
    data: DatasetCreate,
    db: AsyncSession = Depends(get_db),  # noqa: B008
) -> DatasetRead:
    # TODO: enforce role-based auth once auth setup is stable
    return await DatasetService.create(db, data)


@router.get("/", response_model=list[DatasetRead])
async def list_datasets(db: AsyncSession = Depends(get_db)) -> list[DatasetRead]:  # noqa: B008
    return await DatasetService.list(db)
