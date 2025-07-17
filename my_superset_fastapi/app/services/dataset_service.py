from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Dataset, DatasetColumn, DatasetMetric
from app.schemas.dataset import DatasetCreate


class DatasetService:
    @staticmethod
    async def create(db: AsyncSession, data: DatasetCreate) -> Dataset:
        dataset = Dataset(
            name=data.name,
            database_id=data.database_id,
            schema_name=data.schema_name,
            table_name=data.table_name,
            sql=data.sql,
        )
        db.add(dataset)
        if data.columns:
            for col in data.columns:
                db.add(DatasetColumn(dataset=dataset, name=col))
        if data.metrics:
            for metric in data.metrics:
                db.add(DatasetMetric(dataset=dataset, name=metric, expression=""))
        await db.commit()
        await db.refresh(dataset)
        return dataset

    @staticmethod
    async def list(db: AsyncSession) -> list[Dataset]:
        result = await db.execute(select(Dataset))
        return result.scalars().all()

    @staticmethod
    async def get(db: AsyncSession, dataset_id: int) -> Dataset | None:
        return await db.get(Dataset, dataset_id)
