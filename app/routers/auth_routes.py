from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

# Importacion de Codigo 
from app.backend.database import get_db
from app.models.usuario_model import Usuario
from app.models.profesor_model import Profesor
from app.schemas.usuario_schema import UsuarioLogin
from app.schemas.token_schema  import Token
from app.services.auth_utils import verify_password, create_access_token

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login", response_model=Token)
def login(usuario: UsuarioLogin, db: Session = Depends(get_db)):
    # 1. Verificar si el usuario existe
    db_usuario = db.query(Usuario).filter(Usuario.email == usuario.email).first()
    if not db_usuario:
        raise HTTPException(status_code=400, detail="Email no registrado")

    # 2. Verificar contraseña
    try:
        if not verify_password(usuario.contrasena, db_usuario.contrasena_hash):
            raise HTTPException(status_code=400, detail="Contraseña incorrecta")
    except Exception as e:
        # Si el hash no es válido, verificar si la contraseña está en texto plano
        if usuario.contrasena == db_usuario.contrasena_hash:
            # La contraseña está en texto plano, necesita ser hasheada
            from app.services.auth_utils import get_password_hash
            new_hash = get_password_hash(usuario.contrasena)
            db_usuario.contrasena_hash = new_hash
            db.commit()
        else:
            raise HTTPException(status_code=400, detail="Error en la verificación de contraseña")

    # Consulta manual para ver si ese usuario es profesor
    id_profesor = None
    if db_usuario.rol == "profesor":
        db_profesor = db.query(Profesor).filter(Profesor.id_usuario == db_usuario.id_usuario).first()
        if db_profesor:
            id_profesor = db_profesor.id_profesor

    token = create_access_token({
        "sub": str(db_usuario.id_usuario),
        "rol": db_usuario.rol
    })

    return {
        "access_token": token,
        "token_type": "bearer",
        "rol": db_usuario.rol,
        "correo": db_usuario.email,
        "id": db_usuario.id_usuario,
        "nombres": db_usuario.nombres,
        "apellidos": db_usuario.apellidos,
        "id_profesor": id_profesor  # ← Esto lo agregamos
    }