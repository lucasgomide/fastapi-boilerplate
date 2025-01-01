from pydantic_settings import BaseSettings
from pydantic import model_validator


class Settings(BaseSettings):
    ENV: str = "development"
    DATABASE_URL: str = "postgresql://postgres:@localhost:5432/postgres"
    ASYNC_DATABASE_URL: str | None = None

    @model_validator(mode='after')
    def set_async_database_url(cls, values):
        if values.DATABASE_URL:
            values.ASYNC_DATABASE_URL = values.DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://", 1)
        return values


settings = Settings()
