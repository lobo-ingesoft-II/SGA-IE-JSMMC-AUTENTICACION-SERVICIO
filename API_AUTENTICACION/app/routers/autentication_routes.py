from fastapi import APIRouter # para crear rutas en FastAPI modulares
from fastapi import HTTPException # para manejar excepciones HTTP

from app.backend.session import connection  # Importar la base de datos desde el archivo de sesión
