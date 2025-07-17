from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_db
from app.schemas.chart import ChartCreate, ChartRead
from app.services.chart_service import ChartService

router = APIRouter(prefix="/charts", tags=["charts"])
db_dep = Depends(get_db)


@router.post("/", response_model=ChartRead, status_code=status.HTTP_201_CREATED)
async def create_chart(data: ChartCreate, db: AsyncSession = db_dep) -> ChartRead:
    return await ChartService.create(db, data)


@router.get("/preview/{chart_id}", response_model=ChartRead)
async def preview_chart(chart_id: int, db: AsyncSession = db_dep) -> ChartRead:
    # TODO: return sample data for frontend preview
    chart = await ChartService.get(db, chart_id)
    if not chart:
        raise HTTPException(status_code=404, detail="Chart not found")
    return chart


@router.get("/", response_model=list[ChartRead])
async def list_charts(db: AsyncSession = db_dep) -> list[ChartRead]:
    return await ChartService.list(db)
