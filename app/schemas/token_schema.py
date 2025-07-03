from pydantic import BaseModel, EmailStr

class Token(BaseModel):
    access_token: str
    token_type: str
    rol: str
    correo: str
    id: int
    nombres: str
    apellidos: str
    id_profesor: int | None = None  

    
class TokenData(BaseModel):
    email: str
    rol: str