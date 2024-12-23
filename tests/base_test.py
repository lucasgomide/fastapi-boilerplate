from fastapi.testclient import TestClient
from app.main import app
from unittest import TestCase


class BaseTest(TestCase):
    def setUp(self):
        self.client = TestClient(app)
