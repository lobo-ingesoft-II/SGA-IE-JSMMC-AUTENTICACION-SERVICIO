from fastapi import APIRouter, Depends
from ..dependencies import role_required

router = APIRouter(
    prefix="/profesor",
    tags=["profesor"],
    dependencies=[Depends(role_required("profesor"))]
)

@router.get("/")
def vista_profesor():
    return {"message": "Bienvenido, Profesor"}