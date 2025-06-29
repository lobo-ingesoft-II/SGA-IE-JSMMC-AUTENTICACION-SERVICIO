
from sqlalchemy import Column, Integer, String, Enum, DateTime, Boolean, Date
from app.database import Base 

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
    rol = Column(Enum('administrador', 'acudiente', 'profesor', name='rol_usuario'), 
                 nullable=False)
    estado = Column(Enum('activo', 'inactivo', name='estado_usuario'), 
                   nullable=False, default='activo')
    fecha_creacion = Column(DateTime, nullable=False, server_default='CURRENT_TIMESTAMP')
    fecha_modificacion = Column(DateTime, nullable=False, 
                                server_default='CURRENT_TIMESTAMP', 
                                onupdate='CURRENT_TIMESTAMP')

class Administrador(Base):
    __tablename__ = "administradores"
    
    id_administrador = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, nullable=False, unique=True)

class Acudiente(Base):
    __tablename__ = "acudientes"
    
    id_acudiente = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, nullable=False, unique=True)
    parentesco = Column(String(50))
    celular = Column(String(20))
    direccion = Column(String(150))

class Profesor(Base):
    __tablename__ = "profesores"
    
    id_profesor = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, nullable=False, unique=True)
    especialidad = Column(String(100))
    es_director = Column(Boolean, nullable=False, default=False)

# Estudiante no hace parte de auth_db,
