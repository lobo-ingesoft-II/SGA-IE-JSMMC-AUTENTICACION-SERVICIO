from fastapi import APIRouter, Depends
from ..dependencies import role_required
#Vista opcional si se define alguna vista de estudiantes
router = APIRouter(
    prefix="/estudiante",
    tags=["estudiante"],
    dependencies=[Depends(role_required("estudiante"))]
)

@router.get("/")
def vista_estudiante():
    return {"message": "Bienvenido, Estudiante"}