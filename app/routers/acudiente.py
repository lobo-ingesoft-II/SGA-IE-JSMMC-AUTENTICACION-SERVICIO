from fastapi import APIRouter, Depends
from ..dependencies import role_required
router = APIRouter(
    prefix="/acudiente",
    tags=["acudiente"],
    dependencies=[Depends(role_required("acudiente"))]
)

@router.get("/")
def vista_acudiente():
    return {"message": "Bienvenido, Acudiente"}