from fastapi import FastAPI
from src.core.config import settings
from src.api.v1.api import api_router

app = FastAPI(
    title=settings.app_name,
    version=settings.version,
    debug=settings.debug
)

# Incluir las rutas de la API v1
app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API de Control de Gastos"}

@app.get("/health")
def health_check():
    return {"status": "ok", "version": settings.version}



