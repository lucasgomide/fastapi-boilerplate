from fastapi import APIRouter
from app.serializers import UserSerializer
from app.db import get_session
from app.models.user import User
from sqlmodel import select

router = APIRouter()


@router.get("/users", response_model=list[UserSerializer])
async def list_users() -> dict:
    with get_session() as session:
        stmt = select(User.username)
        return session.execute(stmt).mappings()
