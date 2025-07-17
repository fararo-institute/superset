from datetime import datetime

from pydantic import BaseModel


class DatasetBase(BaseModel):
    name: str
    database_id: int | None = None
    schema_name: str | None = None
    table_name: str | None = None
    sql: str | None = None


class DatasetCreate(DatasetBase):
    columns: list[str] | None = None  # TODO: replace with proper objects
    metrics: list[str] | None = None


class DatasetRead(DatasetBase):
    id: int
    created_at: datetime
    columns: list[str] | None = None
    metrics: list[str] | None = None

    class Config:
        orm_mode = True
