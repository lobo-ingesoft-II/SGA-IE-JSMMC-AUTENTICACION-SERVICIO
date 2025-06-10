from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt
# Importa componentes del módulo de autenticación local de la aplicación
from app.auth import oauth2_scheme, SECRET_KEY, ALGORITHM
import os


# Esta función se encarga de obtener el usuario actual a partir del token JWT
async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No autorizado",
    )
    try:
        # Se decodifica el JWT usando la clave secreta y el algoritmo especificado
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])  # Usa la variable importada
        # Se extraen los campos "sub" (usualmente el correo) y "rol" del payload del JWT
        email: str = payload.get("sub")
        rol: str = payload.get("rol")
        # Si no están presentes, se lanza la excepción de credenciales inválidas
        if email is None or rol is None:
            raise credentials_exception
        # Si todo va bien, se retorna un diccionario con los datos del usuario
        return {"email": email, "rol": rol}
    except JWTError:
        raise credentials_exception

# Esta función es un decorador para proteger rutas por rol
def role_required(required_rol: str):
    def role_checker(current_user: dict = Depends(get_current_user)):
        # Si el rol del usuario actual no coincide con el requerido, lanza error 403
        if current_user["rol"] != required_rol:
            raise HTTPException(status_code=403, detail="Acceso prohibido")
        # Si el rol es correcto, se permite continuar con el usuario actual
        return current_user
    return role_checker