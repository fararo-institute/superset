from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.chart import Chart
from app.schemas.chart import ChartCreate


class ChartService:
    @staticmethod
    async def create(db: AsyncSession, data: ChartCreate) -> Chart:
        chart = Chart(
            name=data.name,
            dataset_id=data.dataset_id,
            chart_type=data.chart_type,
            config=data.config,
        )
        db.add(chart)
        await db.commit()
        await db.refresh(chart)
        return chart

    @staticmethod
    async def list(db: AsyncSession) -> list[Chart]:
        result = await db.execute(select(Chart))
        return result.scalars().all()

    @staticmethod
    async def get(db: AsyncSession, chart_id: int) -> Chart | None:
        return await db.get(Chart, chart_id)
