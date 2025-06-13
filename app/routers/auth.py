from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Usuario
from ..schemas import UsuarioLogin, Token
from ..auth import verify_password, create_access_token

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login", response_model=Token)
def login(usuario: UsuarioLogin, db: Session = Depends(get_db)):
    # 1. Verificar si el usuario existe
    db_usuario = db.query(Usuario).filter(Usuario.email == usuario.email).first()
    if not db_usuario:
        raise HTTPException(status_code=400, detail="Email no registrado")

    # 2. Verificar contraseña
    if not verify_password(usuario.contrasena, db_usuario.contrasena_hash):
        raise HTTPException(status_code=400, detail="Contraseña incorrecta")

    # 3. Generar token JWT con el rol
    token = create_access_token(
        data={"sub": db_usuario.email, "rol": db_usuario.rol}
    )

    return {
        "access_token": token,
        "token_type": "bearer",
        "rol": db_usuario.rol, # Enviamos el rol para redirección en frontend
        "correo": db_usuario.email,
        "id": db_usuario.id_usuario
    }