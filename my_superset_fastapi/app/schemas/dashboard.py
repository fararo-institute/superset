from datetime import datetime

from pydantic import BaseModel


class DashboardBase(BaseModel):
    title: str
    layout: str | None = None
    filters: str | None = None


class DashboardCreate(DashboardBase):
    share_token: str | None = None


class DashboardRead(DashboardBase):
    id: int
    share_token: str | None = None
    created_at: datetime

    class Config:
        orm_mode = True
