# API Control de Gastos

API desarrollada con FastAPI para el control de gastos personales.

## Estructura de Carpetas

```
src/
├── api/                    # Rutas de la API
│   ├── v1/                # Versión 1 de la API
│   │   ├── endpoints/     # Endpoints específicos
│   │   │   ├── gastos.py  # Endpoints para gastos
│   │   │   ├── categorias.py (futuro)
│   │   │   └── usuarios.py (futuro)
│   │   └── api.py         # Router principal de la API v1
├── core/                   # Configuraciones centrales
│   ├── config.py          # Configuraciones de la aplicación
│   └── database.py        # Configuración de base de datos (futuro)
├── models/                 # Modelos de base de datos
│   └── gastos.py          # Modelo de gastos (futuro)
├── schemas/                # Esquemas Pydantic
│   └── gastos.py          # Esquemas para gastos (futuro)
└── services/               # Lógica de negocio
    └── gastos_service.py  # Servicios para gastos (futuro)
```

## Cómo Crear Nuevos Módulos

### 1. Crear un nuevo endpoint

1. Crea un archivo en `src/api/v1/endpoints/` (ej: `categorias.py`)
2. Define tus rutas usando `APIRouter()`
3. Registra el router en `src/api/v1/api.py`

### 2. Crear nuevos esquemas

1. Crea un archivo en `src/schemas/` (ej: `categorias.py`)
2. Define tus modelos Pydantic

### 3. Crear nuevos servicios

1. Crea un archivo en `src/services/` (ej: `categorias_service.py`)
2. Implementa la lógica de negocio

## Endpoints Disponibles

- `GET /` - Página principal
- `GET /health` - Verificación de salud
- `GET /api/v1/gastos/` - Obtener todos los gastos
- `POST /api/v1/gastos/` - Crear un nuevo gasto
- `GET /api/v1/gastos/{id}` - Obtener un gasto específico

## Ejecutar la API

```bash
uvicorn main:app --reload
```

## Documentación

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc 