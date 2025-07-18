from pydantic import BaseModel, Field # esta librería permite definir modelos de datos y validarlos automáticamente

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
