from sqlalchemy import Column, Integer, String, Enum, DateTime, Boolean, ForeignKey, Date
from sqlalchemy.orm import relationship
from app.backend.session import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id_usuario = Column(Integer, primary_key=True, index=True)
    nombres = Column(String(50), nullable=False)
    apellidos = Column(String(50), nullable=False)
    tipo_documento = Column(String(20), nullable=False)
    documento_identidad = Column(String(20), nullable=False, unique=True)
    telefono = Column(String(20))
    email = Column(String(100), nullable=False, unique=True)
    contrasena_hash = Column(String(255), nullable=False)
    rol = Column(Enum('administrador', 'acudiente', 'profesor', name='rol_usuario'), nullable=False)
    estado = Column(Enum('activo', 'inactivo', name='estado_usuario'), nullable=False, default='activo')
    fecha_creacion = Column(DateTime, nullable=False, server_default='CURRENT_TIMESTAMP')
    fecha_modificacion = Column(DateTime, nullable=False, server_default='CURRENT_TIMESTAMP', onupdate='CURRENT_TIMESTAMP')


# class Usuario(Base):
#     __tablename__ = "usuarios"

#     id_usuario = Column(Integer, primary_key=True, index=True)
#     nombres = Column(String(50), nullable=False)
#     apellidos = Column(String(50), nullable=False)
#     tipo_documento = Column(String(20), nullable=False)
#     documento_identidad = Column(String(20), nullable=False, unique=True)
#     telefono = Column(String(20))
#     email = Column(String(100), nullable=False, unique=True)
#     contrasena_hash = Column(String(255), nullable=False)
#     rol = Column(Enum('administrador', 'acudiente', 'profesor', name='rol_usuario'), 
#                nullable=False)
#     estado = Column(Enum('activo', 'inactivo', name='estado_usuario'), 
#                    nullable=False, default='activo')
#     fecha_creacion = Column(DateTime, nullable=False, server_default='CURRENT_TIMESTAMP')
#     fecha_modificacion = Column(DateTime, nullable=False, 
#                               server_default='CURRENT_TIMESTAMP', 
#                               onupdate='CURRENT_TIMESTAMP')
    

#     # Relaciones con tablas específicas de roles
#     administrador = relationship("Administrador", back_populates="usuario", uselist=False)
#     acudiente = relationship("Acudiente", back_populates="usuario", uselist=False)
#     profesor = relationship("Profesor", back_populates="usuario", uselist=False)
#     estudiante = relationship("Estudiante", back_populates="usuario", uselist=False)



# # Al final del archivo usuario se importa los otros modelos para los mapeos 
# from app.models.administrador_model import Administrador
# from app.models.acudiente_model import Acudiente
# from app.models.profesor_model import Profesor
# from app.models.estudiante_model import Estudiante
