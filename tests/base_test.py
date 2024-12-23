from sqlalchemy import orm
from app.db import engine, get_session
from app.conf import settings
from fastapi.testclient import TestClient
from sqlmodel import SQLModel

from alembic.config import Config
from alembic import command
from app.main import app
from unittest import TestCase


SessionFactory = orm.scoped_session(orm.sessionmaker(engine))


class BaseTest(TestCase):
    session = None

    def setUp(self):
        self._run_migrations()
        self.session = SessionFactory()

        def get_session_override():
            return self.session

        app.dependency_overrides[get_session] = get_session_override

        self.client = TestClient(app)

    def tearDown(self):
        self.session.rollback()
        SessionFactory.remove()
        app.dependency_overrides.clear()
        SQLModel.metadata.drop_all(bind=engine)

    @staticmethod
    def _run_migrations():
        alembic_cfg = Config()
        alembic_cfg.set_main_option("script_location", "migrations")
        alembic_cfg.set_main_option("sqlalchemy.url", settings.DATABASE_URL)

        command.upgrade(alembic_cfg, "head")
        SQLModel.metadata.create_all(bind=engine)
