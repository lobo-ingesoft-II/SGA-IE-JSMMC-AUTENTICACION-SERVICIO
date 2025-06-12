from sqlalchemy import Column, Integer, String, Enum, DateTime, Boolean, ForeignKey, Date
from sqlalchemy.orm import relationship
from app.backend.session import Base

class Profesor(Base):
    __tablename__ = "profesores"
    
    id_profesor = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=False, unique=True)
    especialidad = Column(String(100))
    es_director = Column(Boolean, nullable=False, default=False)
    
    usuario = relationship("Usuario", back_populates="profesor")
