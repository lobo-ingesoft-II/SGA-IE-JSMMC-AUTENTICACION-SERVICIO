from sqlalchemy import Column, Integer, String, Enum, DateTime, Boolean, ForeignKey, Date
from sqlalchemy.orm import relationship
from app.backend.session import Base


class Acudiente(Base):
    __tablename__ = "acudientes"

    id_acudiente = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, nullable=False, unique=True)
    parentesco = Column(String(50))
    celular = Column(String(20))
    direccion = Column(String(150))


# class Acudiente(Base):
#     __tablename__ = "acudientes"
    
#     id_acudiente = Column(Integer, primary_key=True, index=True)
#     id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=False, unique=True)
#     parentesco = Column(String(50))
#     celular = Column(String(20))
#     direccion = Column(String(150))
    
#     usuario = relationship("Usuario", back_populates="acudiente")
#     estudiantes = relationship("Estudiante", back_populates="acudiente")


# # Al final del archivo se importa los otros modelos para los mapeos 
# from app.models.estudiante_model import Estudiante
# from app.models.usuario_model import Usuario