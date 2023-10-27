# models/cliente.py

from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Cliente(Base):
    __tablename__ = "clientes"
    
    id = Column(Integer, primary_key=True, index=True)
    nombres = Column(String(50), default=None)
    apellidos = Column(String(50), default=None)
    cui = Column(String(50), default=None)
    puntos = Column(Float, default=None)
    created_at = Column(Date, nullable=False)
    updated_at = Column(Date)


