from pydantic import BaseModel
from typing import Optional

class ProfesorBase(BaseModel):
    id_usuario: int
    especialidad: Optional[str] = None
    es_director: bool

class ProfesorOut(ProfesorBase):
    id_profesor: int

    class Config:
        orm_mode = True