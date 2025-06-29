from sqlalchemy import Column, Integer, String
from app.backend.session import Base

class Acudiente(Base):
    __tablename__ = "acudientes"

    id_acudiente = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, nullable=False, unique=True)
    parentesco = Column(String(50))
    celular = Column(String(20))
    direccion = Column(String(150))
