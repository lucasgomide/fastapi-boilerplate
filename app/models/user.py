from app.models import BaseModel


class User(BaseModel, table=True):
    username: str
