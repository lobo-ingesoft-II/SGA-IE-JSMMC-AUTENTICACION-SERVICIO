from sqlalchemy import Column, Integer, String, Enum, DateTime, Boolean, ForeignKey, Date
from sqlalchemy.orm import relationship
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

    # Relaciones con tablas específicas de roles
    administrador = relationship("Administrador", back_populates="usuario", uselist=False)
    acudiente = relationship("Acudiente", back_populates="usuario", uselist=False)
    profesor = relationship("Profesor", back_populates="usuario", uselist=False)
    estudiante = relationship("Estudiante", back_populates="usuario", uselist=False)

class Administrador(Base):
    __tablename__ = "administradores"
    
    id_administrador = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=False, unique=True)
    
    usuario = relationship("Usuario", back_populates="administrador")

class Acudiente(Base):
    __tablename__ = "acudientes"
    
    id_acudiente = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=False, unique=True)
    parentesco = Column(String(50))
    celular = Column(String(20))
    direccion = Column(String(150))
    
    usuario = relationship("Usuario", back_populates="acudiente")
    estudiantes = relationship("Estudiante", back_populates="acudiente")

class Profesor(Base):
    __tablename__ = "profesores"
    
    id_profesor = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=False, unique=True)
    especialidad = Column(String(100))
    es_director = Column(Boolean, nullable=False, default=False)
    
    usuario = relationship("Usuario", back_populates="profesor")

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