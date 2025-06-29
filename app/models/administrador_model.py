
from sqlalchemy import Column, Integer
from app.backend.session import Base

class Administrador(Base):
    __tablename__ = "administradores"

    id_administrador = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, nullable=False, unique=True)
