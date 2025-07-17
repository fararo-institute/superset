from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_db
from app.schemas.dashboard import DashboardCreate, DashboardRead
from app.services.dashboard_service import DashboardService

router = APIRouter(prefix="/dashboards", tags=["dashboards"])
db_dep = Depends(get_db)


@router.post("/", response_model=DashboardRead, status_code=status.HTTP_201_CREATED)
async def create_dashboard(
    data: DashboardCreate, db: AsyncSession = db_dep
) -> DashboardRead:
    return await DashboardService.create(db, data)


@router.get("/", response_model=list[DashboardRead])
async def list_dashboards(db: AsyncSession = db_dep) -> list[DashboardRead]:
    return await DashboardService.list(db)


@router.get("/preview/{dashboard_id}", response_model=DashboardRead)
async def preview_dashboard(
    dashboard_id: int, db: AsyncSession = db_dep
) -> DashboardRead:
    # TODO: return layout with chart data for preview
    dashboard = await DashboardService.get(db, dashboard_id)
    if not dashboard:
        raise HTTPException(status_code=404, detail="Dashboard not found")
    return dashboard
