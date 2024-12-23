from fastapi import APIRouter, Depends
from app.schemas import UserSchema
from app.db import get_async_session, AsyncSession
from app.models.user import User
from sqlmodel import select

router = APIRouter()


@router.get("/users", response_model=list[UserSchema])
async def list_users(session: AsyncSession = Depends(get_async_session)) -> dict:
        stmt = select(User.username)
        return await session.execute(stmt)
