from datetime import datetime

from pydantic import BaseModel


class DatabaseBase(BaseModel):
    name: str
    sqlalchemy_uri: str


class DatabaseCreate(DatabaseBase):
    pass


class DatabaseRead(DatabaseBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
