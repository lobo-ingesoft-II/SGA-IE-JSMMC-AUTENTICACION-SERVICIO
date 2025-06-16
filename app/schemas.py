from pydantic import BaseModel, EmailStr

class UsuarioLogin(BaseModel):
    email: str
    contrasena: str

class Token(BaseModel):
    access_token: str
    token_type: str
    rol: str  # Añadimos el rol al token
    correo: str #
    id: int
    

class TokenData(BaseModel):
    email: str
    rol: str