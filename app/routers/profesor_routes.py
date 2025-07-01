from fastapi import APIRouter, Depends
from app.services.auth_service import role_required
from app.backend.database import get_db
from app.models.profesor_model import Profesor
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/profesor",
    tags=["profesor"],
    dependencies=[Depends(role_required("profesor"))]
)

@router.get("/")
def vista_profesor():
    return {"message": "Bienvenido, Profesor"}

@router.get("/{id_profesor}")
def get_profesor(id_profesor: int, db: Session = Depends(get_db)):
    dic_curso = db.query(Profesor).filter(Profesor.id_profesor == id_profesor).first()
    if dic_curso:
        return dic_curso
    else:
        return {"message": "Profesor no encontrado"}, 404