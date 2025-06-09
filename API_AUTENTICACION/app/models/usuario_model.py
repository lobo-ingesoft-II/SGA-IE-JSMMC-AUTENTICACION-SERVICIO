from sqlalchemy import Column, Integer, String, DateTime
from app.backend.session import Base

class UsuarioModel(Base):
    __tablename__ = "usuarios"
    id_usuario = Column(Integer, primary_key=True, autoincrement=True)
    nombres = Column(String(50))
    apellidos = Column(String(50))
    tipo_documento = Column(String(20))
    documento_identidad = Column(String(20))
    telefono = Column(String(20))
    email = Column(String(100))
    contrasena_hash = Column(String(255))
    rol = Column(String(20))      # Si tu ENUM tiene valores fijos, puedes usar Enum en SQLAlchemy
    estado = Column(String(20))   # Igual para estado
    fecha_creacion = Column(DateTime)
    fecha_modificacion = Column(DateTime)