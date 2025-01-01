from fastapi import FastAPI

from app.views import users
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(version="v1", root_path="/api")
app.include_router(users.router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
