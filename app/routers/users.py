from fastapi import APIRouter
from app.serializers import UserSerializer

router = APIRouter()


@router.get("/users", response_model=list[UserSerializer])
async def list_users() -> dict:
    return [{"username": "Rick"}, {"username": "Morty"}]
