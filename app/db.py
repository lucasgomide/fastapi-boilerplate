from typing import Generator, AsyncGenerator
from contextlib import contextmanager
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine
from app.conf import settings
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

is_development = settings.ENV in ["development", "test"]

engine = create_engine(url=settings.DATABASE_URL, echo=is_development)
async_engine = create_async_engine(
    url=settings.ASYNC_DATABASE_URL, 
    echo=is_development
)

@contextmanager
def get_session() -> Generator[Session, None, None]:
    session = sessionmaker(bind=engine, expire_on_commit=False)()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with sessionmaker(
        bind=async_engine, expire_on_commit=False, class_=AsyncSession
    )() as session:
        yield session
