from fastapi import FastAPI

from app.routers import users

middleware = None  # define middleware list

app = FastAPI(version="v1", middleware=middleware, root_path="/api")

app.include_router(users.router)
