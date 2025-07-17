from app.core.db import engine
from app.models.base import Base
from fastapi.testclient import TestClient
from main import create_app

app = create_app()


async def setup_database() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.on_event("startup")
async def on_startup() -> None:
    await setup_database()


def test_health() -> None:
    with TestClient(app) as client:
        response = client.get("/api/v1/datasets")
        assert response.status_code == 200
