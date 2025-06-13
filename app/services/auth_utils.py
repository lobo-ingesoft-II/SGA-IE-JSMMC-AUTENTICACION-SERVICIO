from jose import JWTError, jwt               # Para generar/validar tokens JWT
from datetime import datetime, timedelta     # Para manejar fechas/expiración
from fastapi.security import OAuth2PasswordBearer  # Esquema OAuth2 para FastAPI
from passlib.context import CryptContext     # Para hashear/verificar contraseñas
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = "clave_secreta_64_caracteres_1234567890abcdef1234567890abcdef1234567890abcd" # Clave para firmar tokens de prueba (mas adelante la cambiamos y no la mostramos en el codigo publico)
ALGORITHM = "HS256" # Algoritmo de encriptación
ACCESS_TOKEN_EXPIRE_MINUTES = 30 # Tiempo de vida del token

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto") # Configura bcrypt para hashear/verificar contraseñas
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")  #Define la URL donde FastAPI espera recibir credenciales (/auth/login).

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt