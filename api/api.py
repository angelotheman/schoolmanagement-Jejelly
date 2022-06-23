from fastapi import APIRouter
from api.endpoints import student
api_router= APIRouter

api_router.include_router(student.router,prefix='/students',tags=['students'])