from pydantic import BaseModel, EmailStr
from typing import Optional, Literal
from datetime import date, datetime

class AcudienteSchema(BaseModel):
    nombre: str
    apellido: str
    documento: str
    tipo_documento: Literal["CC", "TI", "CE", "PA"]
    fecha_nacimiento: date
    telefono: Optional[str]
    email: Optional[EmailStr]
    direccion: Optional[str]
    parentesco: Literal["Padre", "Madre", "Tío", "Tía", "Abuelo", "Abuela", "Otro"]
    fecha_registro: Optional[datetime]