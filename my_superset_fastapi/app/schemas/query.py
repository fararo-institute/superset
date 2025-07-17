from datetime import datetime

from pydantic import BaseModel


class QueryCreate(BaseModel):
    sql: str
    database_id: int


class QueryRead(QueryCreate):
    id: int
    status: str
    result: str | None = None
    error: str | None = None
    rows: int | None = None
    started_at: datetime | None = None
    finished_at: datetime | None = None

    class Config:
        orm_mode = True
