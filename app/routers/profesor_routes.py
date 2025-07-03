from fastapi import APIRouter, Depends
from app.services.auth_service import role_required
from app.backend.database import get_db
from app.models.profesor_model import Profesor
from sqlalchemy.orm import Session
from http import HTTPException

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
    profesor = db.query(Profesor).filter(Profesor.id_profesor == id_profesor).first()
    if not profesor:
        raise HTTPException(status_code=404, detail="Profesor no encontrado")
    return {"id_profesor": profesor.id_profesor, "id_usuario": profesor.id_usuario, "especialidad": profesor.especialidad, "es_director": profesor.es_director}
    

# # Obtener usuario por ID
# @router.get("/profesores/{id_profesor}")
# def get_profesor(id_profesor: int, db: Session = Depends(get_db)):
#     # Buscar el profesor por ID
#     profesor = db.query(Profesor).filter(Profesor.id_profesor == id_profesor).first()
#     if not profesor:
#         raise HTTPException(status_code=404, detail="Profesor no encontrado")
    
#     # Buscar el usuario asociado manualmente
#     usuario = db.query(UsuarioModel).filter(UsuarioModel.id_usuario == profesor.id_usuario).first()
#     if not usuario:
#         raise HTTPException(status_code=404, detail="Usuario asociado no encontrado")

#     # Combinar los datos de profesor y usuario en un solo dict
#     return {
#         "id_profesor": profesor.id_profesor,
#         "id_usuario": profesor.id_usuario,
#         "especialidad": profesor.especialidad,
#         "es_director": profesor.es_director,
#         "nombres": usuario.nombres,
#         "apellidos": usuario.apellidos,
#         "tipo_documento": usuario.tipo_documento,
#         "documento_identidad": usuario.documento_identidad,
#         "telefono": usuario.telefono,
#         "email": usuario.email,
#         "rol": usuario.rol,
#         "estado": usuario.estado,
#         "fecha_creacion": usuario.fecha_creacion,
#         "fecha_modificacion": usuario.fecha_modificacion
#     }