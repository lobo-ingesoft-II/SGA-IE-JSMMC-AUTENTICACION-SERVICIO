from sqlalchemy import Column, Integer, String, Enum, DateTime, Boolean, ForeignKey, Date
from sqlalchemy.orm import relationship
from app.backend.session import Base

class Administrador(Base):
    __tablename__ = "administradores"
    
    id_administrador = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=False, unique=True)
    
    usuario = relationship("Usuario", back_populates="administrador")


# Al final del archivo se importa los otros modelos para los mapeos 
from app.models.usuario_model import Usuario