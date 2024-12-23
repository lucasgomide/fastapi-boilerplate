import factory
from app.models.user import User
from tests.base_test import SessionFactory


class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = User
        sqlalchemy_session = SessionFactory

    username = factory.Faker("name")
