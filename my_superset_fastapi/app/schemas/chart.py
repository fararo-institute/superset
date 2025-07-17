from datetime import datetime

from pydantic import BaseModel


class ChartBase(BaseModel):
    name: str
    dataset_id: int
    chart_type: str | None = None
    config: str | None = None


class ChartCreate(ChartBase):
    pass


class ChartRead(ChartBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
