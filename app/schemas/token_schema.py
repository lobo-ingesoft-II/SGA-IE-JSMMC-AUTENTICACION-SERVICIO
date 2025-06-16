from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str
    rol: str
    correo: str
    id: int
    nombres: str
    apellidos: str

class TokenData(BaseModel):
    email: str
    rol: str
