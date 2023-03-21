from fastapi import APIRouter
from .endpoint import users

api_router = APIRouter()

api_router.include_router(users.router,prefix='/users')
