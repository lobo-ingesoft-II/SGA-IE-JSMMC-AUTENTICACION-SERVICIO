from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str
    rol: str
    correo: str  # <-- Añadido
    id: int      # <-- Añadido

class TokenData(BaseModel):
    email: str
    rol: str
