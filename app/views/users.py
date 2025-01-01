from fastapi import APIRouter, Depends
from app.views.schemas import UserSchema
from app.db import get_async_session, AsyncSession
from app.models.user import User
from sqlmodel import select
from sqlalchemy.engine import Result

router = APIRouter()


@router.get("/users", response_model=list[UserSchema])
async def list_users(session: AsyncSession = Depends(get_async_session)) -> Result:
        query = select(User.username)
        return await session.execute(query)
