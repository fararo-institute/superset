from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.dashboard import Dashboard
from app.schemas.dashboard import DashboardCreate


class DashboardService:
    @staticmethod
    async def create(db: AsyncSession, data: DashboardCreate) -> Dashboard:
        dashboard = Dashboard(
            title=data.title,
            layout=data.layout,
            filters=data.filters,
            share_token=data.share_token,
        )
        db.add(dashboard)
        await db.commit()
        await db.refresh(dashboard)
        return dashboard

    @staticmethod
    async def list(db: AsyncSession) -> list[Dashboard]:
        result = await db.execute(select(Dashboard))
        return result.scalars().all()

    @staticmethod
    async def get(db: AsyncSession, dashboard_id: int) -> Dashboard | None:
        return await db.get(Dashboard, dashboard_id)
