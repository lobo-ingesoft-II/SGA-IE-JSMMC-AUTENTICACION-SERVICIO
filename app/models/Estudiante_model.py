from sqlalchemy import Column, Integer, String, Enum, DateTime, Boolean, ForeignKey, Date
from sqlalchemy.orm import relationship
from app.backend.session import Base

class Estudiante(Base):
    __tablename__ = "estudiantes"
    
    id_estudiante = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"), unique=True)
    id_acudiente = Column(Integer, ForeignKey("acudientes.id_acudiente"))
    fecha_nacimiento = Column(Date)
    estado_matricula = Column(Enum('pre-matriculado', 'matriculado', 'retirado', 
                                 name='estado_matricula'), 
                            default='pre-matriculado')
    
    usuario = relationship("Usuario", back_populates="estudiante")
    acudiente = relationship("Acudiente", back_populates="estudiantes")


# Al final del archivo se importa los otros modelos para los mapeos 
from app.models.acudiente_model import Acudiente
from app.models.usuario_model import Usuario