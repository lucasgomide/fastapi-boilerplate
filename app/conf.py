from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ENV: str = "development"
    DATABASE_URL: str = "postgresql://lucasgomide:@localhost:5432/postgres"


settings = Settings()
