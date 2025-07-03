from fastapi import APIRouter, Depends
from app.services.auth_service import role_required

router = APIRouter(
    prefix="/admin",
    tags=["admin"]
    # dependencies=[Depends(role_required("administrador"))]  # Se le quita la utenticación de Rol 
)

@router.get("/dashboard")
def admin_dashboard():
    return {"message": "Bienvenido, Administrador"}