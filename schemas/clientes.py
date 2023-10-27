# models/schemas/cliente.py

from pydantic import BaseModel

class ClienteCreate(BaseModel):
    nombres: str
    apellidos: str
    cui: str
    puntos: float
    created_at: str

class ClienteUpdate(BaseModel):
    # nombres: str = None
    # apellidos: str = None
    # cui: str = None
    puntos: float = None