# JWT (JSON Web Token) es un formato estándar para representar tokens de acceso de forma segura 
# y compacta. Se usa comúnmente en autenticación y autorización, especialmente en APIs 
# modernas (como REST o GraphQL).

# bcrypt es un algoritmo de cifrado de contraseñas diseñado específicamente para ser seguro 
# contra ataques de fuerza bruta y diccionario. Es ampliamente usado para proteger
# contraseñas en aplicaciones web.

# Hashear contraseñas con bcrypt al registrar.
# Verificar contraseñas con bcrypt al iniciar sesión.
# Usar JWT para manejar la sesión.

from fastapi import APIRouter # para crear rutas en FastAPI modulares
from fastapi import HTTPException # para manejar excepciones HTTP

from app.backend.session import connection  # Importar la base de datos desde el archivo de sesión
from app.schemas.usuario_schema import Usuario


router = APIRouter() 

# | POST   | `/register`        | Registro de nuevos usuarios      |
@router.post("/register")
def post_registerUser(document:Usuario):

    # verificar que el documento tenga los campos necesarios 
        # No se hace porque el modelo PreRegistrationModel ya tiene los campos necesarios definidos y validados

    

    return True


# | POST   | `/login`           | Autenticación e inicio de sesión |