from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    """Configuraciones de la aplicación"""
    app_name: str = "API Control de Gastos"
    version: str = "1.0.0"
    debug: bool = True
    
    # Configuraciones de base de datos (para futuro uso)
    database_url: Optional[str] = None
    
    class Config:
        env_file = ".env"

settings = Settings() 