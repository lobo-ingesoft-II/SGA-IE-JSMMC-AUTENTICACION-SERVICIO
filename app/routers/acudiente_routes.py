

from fastapi import APIRouter # para crear rutas en FastAPI modulares
from fastapi import APIRouter, Depends
from fastapi import HTTPException # para manejar excepciones HTTP
from fastapi import Depends
from app.services.auth_service import role_required

from app.models.usuario_model import Usuario
from app.schemas.acudiente_schema import AcudienteBase

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

@router.post("/register", status_code=201)
def registrar_acudiente(data: AcudienteBase, db: Session = Depends(get_db)):
    # 1. Verificar que el usuario existe
    usuario = db.query(Usuario).filter(Usuario.id_usuario == data.id_usuario).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="El usuario no existe.")

    # 2. Verificar que el rol del usuario sea 'acudiente'
    if usuario.rol != "acudiente":
        raise HTTPException(status_code=400, detail="El usuario no tiene el rol de acudiente.")

    # 3. Verificar que no haya ya un acudiente asociado
    acudiente_existente = db.query(Acudiente).filter(Acudiente.id_usuario == data.id_usuario).first()
    if acudiente_existente:
        raise HTTPException(status_code=400, detail="El acudiente ya fue registrado.")

    # 4. Crear el nuevo acudiente
    nuevo_acudiente = Acudiente(
        id_usuario=data.id_usuario,
        parentesco=data.parentesco,
        celular=data.celular,
        direccion=data.direccion
    )

    db.add(nuevo_acudiente)
    db.commit()
    db.refresh(nuevo_acudiente)

    return {
        "mensaje": "Acudiente registrado correctamente.",
        "id_acudiente": nuevo_acudiente.id_acudiente
    }