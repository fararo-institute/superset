from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    APP_NAME: str = "My Superset FastAPI"
    DEBUG: bool = False
    SECRET_KEY: str = "change-this-key"  # noqa: S105
    DATABASE_URL: str = "sqlite+aiosqlite:///./app.db"
    CELERY_BROKER_URL: str = "redis://localhost:6379/0"
    CELERY_RESULT_BACKEND: str = "redis://localhost:6379/1"
    ALLOWED_ORIGINS: list[str] = []
    RATE_LIMIT: str | None = "100/minute"


@lru_cache()
def get_settings() -> Settings:
    return Settings()
