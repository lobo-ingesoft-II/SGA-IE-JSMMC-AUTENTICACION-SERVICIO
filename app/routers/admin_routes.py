from fastapi import APIRouter, Depends
from app.services.auth_service import role_required

router = APIRouter(
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(role_required("administrador"))]  # Todas las rutas requieren rol admin
)

@router.get("/dashboard")
def admin_dashboard():
    return {"message": "Bienvenido, Administrador"}