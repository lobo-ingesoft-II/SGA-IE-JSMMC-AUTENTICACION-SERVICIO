from pydantic import BaseModel
from typing import Optional

class AcudienteBase(BaseModel):
    id_usuario: int
    parentesco: Optional[str] = None
    celular: Optional[str] = None
    direccion: Optional[str] = None

class AcudienteOut(AcudienteBase):
    id_acudiente: int

    class Config:
        orm_mode = True