from fastapi import APIRouter
from .endpoints import gastos

api_router = APIRouter()

# Incluir todos los routers de endpoints
api_router.include_router(gastos.router, prefix="/gastos", tags=["gastos"]) 