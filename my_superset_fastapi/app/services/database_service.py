from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from app.models.database import Database
from app.schemas.database import DatabaseCreate


class DatabaseService:
    @staticmethod
    async def create(db: AsyncSession, data: DatabaseCreate) -> Database:
        database = Database(name=data.name, sqlalchemy_uri=data.sqlalchemy_uri)
        db.add(database)
        await db.commit()
        await db.refresh(database)
        return database

    @staticmethod
    async def test_connection(data: DatabaseCreate) -> None:
        engine = create_async_engine(data.sqlalchemy_uri)
        try:
            async with engine.connect() as conn:
                await conn.execute(text("SELECT 1"))
        finally:
            await engine.dispose()

    @staticmethod
    async def introspect_schema(
        db: AsyncSession, database_id: int
    ) -> dict[str, list[str]]:
        database = await db.get(Database, database_id)
        if not database:
            return {}
        engine = create_async_engine(database.sqlalchemy_uri)
        metadata = {}
        try:
            async with engine.connect() as conn:
                result = await conn.run_sync(lambda c: c.dialect.get_table_names(c))
                metadata["tables"] = result
        finally:
            await engine.dispose()
        return metadata
