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
from fastapi import Depends

from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.backend.database import get_db  # Importar la base de datos desde el archivo de sesión

# Importacion de esquemas de validacion y modelos para añadir registros a la BD 
from app.models.usuario_model import Usuario as UsuarioModel
from app.models.profesor_model import Profesor
from app.models.acudiente_model import Acudiente
from app.schemas.usuario_schema import Usuario  

router = APIRouter() 


@router.get("/")
def root():
    return {"message": "API de Autenticacion y Roles"}

# POST /register  => Registro de nuevos usuarios    
@router.post("/register")
def post_registerUser(document:Usuario, db: Session = Depends(get_db)):
    try:
        # La verificacion de campos ya la hace Pydantic 

        # Obtener la conexion de la BD 
        # db: Session = Depends(get_db)) Con esa linea se hace una llamada a la funcion get_db() y se crea una dependencia 

        # Convertir el modelo a un diccionario
        document_dict = document.model_dump(by_alias=True) # Convertir el modelo Pydantic a un DIC
        nuevo_usuario = Usuario(**document_dict) # Crear un nuevo usuario con el modelo 
    
        # El id se coloca automaticamente 
        db.add(nuevo_usuario)
        db.commit()
        db.refresh(nuevo_usuario)

        # return {
        #     "msg": "Usuario registrado exitosamente",
        #     "id_usuario": nuevo_usuario.id_usuario,
        #     "usuario": document_dict
        # }
        return nuevo_usuario  # Retornar el documento creado con su ID asignado por MongoDB

    except SQLAlchemyError as e:
        db.close()
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al registrar usuario: {str(e)}")


@router.get("/getUsers")
def getUsers(db: Session = Depends(get_db)):

    try: 
        usuarios = db.query(UsuarioModel).all()
        return usuarios
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener usuarios: {str(e)}")

# Obtener usuario por ID
@router.get("/profesores/{id_profesor}")
def get_profesor(id_profesor: int, db: Session = Depends(get_db)):
    # Buscar el profesor por ID
    profesor = db.query(Profesor).filter(Profesor.id_profesor == id_profesor).first()
    if not profesor:
        raise HTTPException(status_code=404, detail="Profesor no encontrado")
    
    # Buscar el usuario asociado manualmente
    usuario = db.query(UsuarioModel).filter(UsuarioModel.id_usuario == profesor.id_usuario).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario asociado no encontrado")

    # Combinar los datos de profesor y usuario en un solo dict
    return {
        "id_profesor": profesor.id_profesor,
        "id_usuario": profesor.id_usuario,
        "especialidad": profesor.especialidad,
        "es_director": profesor.es_director,
        "nombres": usuario.nombres,
        "apellidos": usuario.apellidos,
        "tipo_documento": usuario.tipo_documento,
        "documento_identidad": usuario.documento_identidad,
        "telefono": usuario.telefono,
        "email": usuario.email,
        "rol": usuario.rol,
        "estado": usuario.estado,
        "fecha_creacion": usuario.fecha_creacion,
        "fecha_modificacion": usuario.fecha_modificacion
    }

# Obtener acudiente por ID
@router.get("/acudientes/{id_acudiente}")
def get_acudiente(id_acudiente: int, db: Session = Depends(get_db)):
    acudiente = db.query(Acudiente).filter(Acudiente.id_acudiente == id_acudiente).first()
    if not acudiente:
        raise HTTPException(status_code=404, detail="Acudiente no encontrado")
    return acudiente
