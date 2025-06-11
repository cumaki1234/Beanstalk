from sqlalchemy import Column, Integer, String, Float
from database import Base
from typing import Any

class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(String(250), nullable=False)
    precio = Column(Float, nullable=False)
