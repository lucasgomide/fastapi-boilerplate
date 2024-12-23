from pydantic import BaseModel


class UserSerializer(BaseModel):
    username: str
