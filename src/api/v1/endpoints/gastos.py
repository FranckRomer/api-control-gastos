from fastapi import APIRouter, HTTPException
from typing import List, Optional
from pydantic import BaseModel

router = APIRouter()

class GastoCreate(BaseModel):
    descripcion: str
    monto: float
    categoria: str
    fecha: str

class GastoResponse(BaseModel):
    id: int
    descripcion: str
    monto: float
    categoria: str
    fecha: str

# Simulación de base de datos
gastos_db = []
contador_id = 1

@router.get("/", response_model=List[GastoResponse])
async def obtener_gastos():
    """Obtener todos los gastos"""
    return gastos_db

@router.post("/", response_model=GastoResponse)
async def crear_gasto(gasto: GastoCreate):
    """Crear un nuevo gasto"""
    global contador_id
    nuevo_gasto = GastoResponse(
        id=contador_id,
        descripcion=gasto.descripcion,
        monto=gasto.monto,
        categoria=gasto.categoria,
        fecha=gasto.fecha
    )
    gastos_db.append(nuevo_gasto)
    contador_id += 1
    return nuevo_gasto

@router.get("/{gasto_id}", response_model=GastoResponse)
async def obtener_gasto(gasto_id: int):
    """Obtener un gasto específico por ID"""
    for gasto in gastos_db:
        if gasto.id == gasto_id:
            return gasto
    raise HTTPException(status_code=404, detail="Gasto no encontrado") 