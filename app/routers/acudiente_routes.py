

from fastapi import APIRouter # para crear rutas en FastAPI modulares
from fastapi import APIRouter, Depends
from fastapi import HTTPException # para manejar excepciones HTTP
from fastapi import Depends
from app.services.auth_service import role_required

from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.backend.database import get_db  # Importar la base de datos desde el archivo de sesión


from app.models.acudiente_model import Acudiente


router = APIRouter(
    prefix="/acudiente",
    tags=["acudiente"]
    # dependencies=[Depends(role_required("acudiente"))] # Se le quita la utenticación de Rol 
) 

@router.get("/")
def vista_acudiente():
    return {"message": "Bienvenido, Acudiente"}


# Obtener acudiente por ID
@router.get("/{id_acudiente}")
def get_acudiente(id_acudiente: int, db: Session = Depends(get_db)):
    acudiente = db.query(Acudiente).filter(Acudiente.id_acudiente == id_acudiente).first()
    if not acudiente:
        raise HTTPException(status_code=404, detail="Acudiente no encontrado")
    return acudiente
