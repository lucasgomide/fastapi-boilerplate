from typing import Generator
from contextlib import contextmanager
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine
from app.conf import settings

engine = create_engine(url=settings.DATABASE_URL)


@contextmanager
def get_session() -> Generator[Session]:
    session = sessionmaker(bind=engine, expire_on_commit=False)()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
