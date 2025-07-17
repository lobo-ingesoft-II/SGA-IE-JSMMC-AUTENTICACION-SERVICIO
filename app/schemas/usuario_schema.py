from pydantic import BaseModel, Field, EmailStr # esta librería permite definir modelos de datos y validarlos automáticamente
from typing import Optional, Dict, Any
# OJO NO NECESITA CONSTRUCTOR, Pydantic maneja la creación de instancias automáticamente
class Usuario(BaseModel):
    nombres: str
    apellidos: str
    tipoDocumento: str = Field(..., alias="tipo_documento")
    documentoIdentidad: str = Field(..., alias="documento_identidad")
    telefono: str
    email: str
    contrasenaHash: str = Field(..., alias="contrasena_hash")
    rol: str
    estado: str
    fechaCreacion: str = Field(..., alias="fecha_creacion")
    fechaModificacion: str = Field(..., alias="fecha_modificacion")

    class Config:
        validate_by_name = True

class Usuario_id(Usuario):
    id : int = Field(..., alias="id_estudiante")


class UsuarioLogin(BaseModel):
    email: str
    contrasena: str
    #rol: str
# Esquema extendido para incluir los datos adicionales en la creación de un usuario
class CrearUsuario(BaseModel):
    nombres: str
    apellidos: str
    tipoDocumento: str = Field(..., alias="tipo_documento")
    documentoIdentidad: str = Field(..., alias="documento_identidad")
    telefono: str
    email: EmailStr
    contrasena: str
    rol: str
    datos_adicionales: Optional[Dict[str, Any]]  # Este campo es para los datos específicos del rol

    class Config:
        orm_mode = True

class UsuarioUpdate(BaseModel):
    nombres: Optional[str] = None
    apellidos: Optional[str] = None
    tipoDocumento: Optional[str] = None
    documentoIdentidad: Optional[str] = None
    telefono: Optional[str] = None
    email: Optional[str] = None
    contrasena: Optional[str] = None
    rol: Optional[str] = None
    datos_adicionales: Optional[dict] = None

class ProfesorResponse(BaseModel):
    id_usuario: int
    id_profesor: int
    nombres: str
    apellidos: str
    email: str
    tipoDocumento: str
    documentoIdentidad: str
    telefono: str

    class Config:
        orm_mode = True

class AcudienteResponse(BaseModel):
    id_usuario: int
    id_acudiente: int
    nombres: str
    apellidos: str
    email: str
    tipoDocumento: str
    documentoIdentidad: str
    telefono: str

    class Config:
        orm_mode = True

class AdministradorResponse(BaseModel):
    id_usuario: int
    id_administrador: int
    nombres: str
    apellidos: str
    email: str
    tipoDocumento: str
    documentoIdentidad: str
    telefono: str

    class Config:
        orm_mode = True