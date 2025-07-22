
from app.services.auth_service import role_required
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.backend.database import get_db
from app.models.usuario_model import Usuario
from app.models.profesor_model import Profesor
from app.models.acudiente_model import Acudiente
from app.models.administrador_model import Administrador
from app.schemas.usuario_schema import CrearUsuario, UsuarioUpdate, ProfesorResponse, AcudienteResponse, AdministradorResponse
from app.services.auth_utils import get_password_hash
from datetime import datetime, timezone, timedelta
from typing import List
router = APIRouter(
    prefix="/admin",
    tags=["admin"]
    # dependencies=[Depends(role_required("administrador"))]  # Se le quita la utenticación de Rol 
)

@router.get("/dashboard")
def admin_dashboard():
    return {"message": "Bienvenido, Administrador"}

# Crear un nuevo usuario
@router.post("/usuarios", status_code=201)
async def crear_usuario(usuario: CrearUsuario, db: Session = Depends(get_db)):
    # Verificar si el documento_identidad o email ya existen
    db_usuario = db.query(Usuario).filter(
        (Usuario.documento_identidad == usuario.documentoIdentidad) | 
        (Usuario.email == usuario.email)
    ).first()
    if db_usuario:
        raise HTTPException(status_code=400, detail="Documento de identidad o email ya existen.")
     # Hashear la contraseña antes de crear el usuario
    contrasena_hash = get_password_hash(usuario.contrasena)  # Hasheamos la contraseña aquí

    # Crear el nuevo usuario
    nuevo_usuario = Usuario(
        nombres=usuario.nombres,
        apellidos=usuario.apellidos,
        tipo_documento=usuario.tipoDocumento,
        documento_identidad=usuario.documentoIdentidad,
        telefono=usuario.telefono,
        email=usuario.email,
        contrasena_hash=contrasena_hash,  # Aquí debes hashear la contraseña
        rol=usuario.rol,
        estado='activo'
    )

    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)

    # Aquí se verifica el rol y se agrega la información adicional
    if usuario.rol == "administrador":
        db.add(Administrador(id_usuario=nuevo_usuario.id_usuario))
    elif usuario.rol == "acudiente":
        if "parentesco" in usuario.datos_adicionales and "celular" in usuario.datos_adicionales:
            db.add(Acudiente(
                id_usuario=nuevo_usuario.id_usuario, 
                parentesco=usuario.datos_adicionales.get('parentesco'),
                celular=usuario.datos_adicionales.get('celular'),
                direccion=usuario.datos_adicionales.get('direccion')
            ))
        else:
            raise HTTPException(status_code=400, detail="Datos adicionales del acudiente incompletos.")
    elif usuario.rol == "profesor":
        if "especialidad" in usuario.datos_adicionales:
            db.add(Profesor(
                id_usuario=nuevo_usuario.id_usuario, 
                especialidad=usuario.datos_adicionales.get('especialidad'),
                es_director=usuario.datos_adicionales.get('es_director', False)
            ))
        else:
            raise HTTPException(status_code=400, detail="Datos adicionales del profesor incompletos.")
    
    db.commit()
    return {"mensaje": "Usuario creado correctamente", "id_usuario": nuevo_usuario.id_usuario}

# Editar un usuario
@router.patch("/usuarios/{id_usuario}")
async def editar_usuario_parcial(id_usuario: int, usuario: UsuarioUpdate, db: Session = Depends(get_db)):
    db_usuario = db.query(Usuario).filter(Usuario.id_usuario == id_usuario).first()
    if not db_usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado.")
    
    if usuario.nombres:
        db_usuario.nombres = usuario.nombres
    if usuario.apellidos:
        db_usuario.apellidos = usuario.apellidos
    if usuario.tipoDocumento:
        db_usuario.tipo_documento = usuario.tipoDocumento
    if usuario.documentoIdentidad:
        db_usuario.documento_identidad = usuario.documentoIdentidad
    if usuario.telefono:
        db_usuario.telefono = usuario.telefono
    if usuario.email:
        db_usuario.email = usuario.email
    if usuario.rol:
        db_usuario.rol = usuario.rol
     # Establecer la fecha de modificación a la hora actual de Colombia
    colombia_timezone = timezone(timedelta(hours=-5))  # Zona horaria de Colombia (UTC-5)
    fecha_modificacion_colombia = datetime.now(colombia_timezone)  # Fecha y hora de Colombia
    db_usuario.fecha_modificacion = fecha_modificacion_colombia  # Actualiza el campo de fecha_modificacion


    db.commit()
    db.refresh(db_usuario)
    
    if usuario.rol == "acudiente" and usuario.datos_adicionales:
        db_acudiente = db.query(Acudiente).filter(Acudiente.id_usuario == id_usuario).first()
        db_acudiente.parentesco = usuario.datos_adicionales.get('parentesco', db_acudiente.parentesco)
        db_acudiente.celular = usuario.datos_adicionales.get('celular', db_acudiente.celular)
        db_acudiente.direccion = usuario.datos_adicionales.get('direccion', db_acudiente.direccion)
    elif usuario.rol == "profesor" and usuario.datos_adicionales:
        db_profesor = db.query(Profesor).filter(Profesor.id_usuario == id_usuario).first()
        db_profesor.especialidad = usuario.datos_adicionales.get('especialidad', db_profesor.especialidad)
        db_profesor.es_director = usuario.datos_adicionales.get('es_director', db_profesor.es_director)

    db.commit()
    return {"mensaje": "Usuario actualizado correctamente"}

# Habilitar o deshabilitar usuario
@router.patch("/usuarios/{id_usuario}/estado")
async def cambiar_estado_usuario(id_usuario: int, estado: str, db: Session = Depends(get_db)):
    if estado not in ["activo", "inactivo"]:
        raise HTTPException(status_code=400, detail="Estado inválido. Debe ser 'activo' o 'inactivo'.")

    db_usuario = db.query(Usuario).filter(Usuario.id_usuario == id_usuario).first()
    if not db_usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado.")
    
    
    db_usuario.estado = estado
    # Obtener la hora actual en la zona horaria de Colombia
    colombia_timezone = timezone(timedelta(hours=-5))  # Zona horaria de Colombia (UTC-5)
    fecha_modificacion_colombia = datetime.now(colombia_timezone)  # Fecha y hora de Colombia

    # Actualizar el campo fecha_modificacion con el valor calculado en Python
    db_usuario.fecha_modificacion = fecha_modificacion_colombia
    db.commit()
    db.refresh(db_usuario)
    
    return {"mensaje": "Estado de usuario actualizado correctamente"}

# Eliminar un usuario
@router.delete("/usuarios/{id_usuario}")
async def eliminar_usuario(id_usuario: int, db: Session = Depends(get_db)):
    db_usuario = db.query(Usuario).filter(Usuario.id_usuario == id_usuario).first()
    if not db_usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado.")

    # Eliminar las asociaciones de las tablas secundarias
    if db_usuario.rol == "administrador":
        db.query(Administrador).filter(Administrador.id_usuario == id_usuario).delete()
    elif db_usuario.rol == "acudiente":
        db.query(Acudiente).filter(Acudiente.id_usuario == id_usuario).delete()
    elif db_usuario.rol == "profesor":
        db.query(Profesor).filter(Profesor.id_usuario == id_usuario).delete()

    # Eliminar el usuario
    db.query(Usuario).filter(Usuario.id_usuario == id_usuario).delete()

    db.commit()
    return {"mensaje": "Usuario eliminado correctamente"}

#Obtener los usuarios por rol
@router.get("/profesores", response_model=List[ProfesorResponse])
def obtener_profesores(db: Session = Depends(get_db)):
    profesores = db.query(
        Usuario.id_usuario,
        Usuario.nombres,
        Usuario.apellidos,
        Usuario.email,
        Usuario.tipo_documento,
        Usuario.documento_identidad,
        Usuario.telefono,
        Usuario.estado,
        Profesor.id_profesor,
    ).join(
        Profesor, Usuario.id_usuario == Profesor.id_usuario
    ).filter(
        Usuario.rol == "profesor"
    ).all()

    return [ProfesorResponse(
        id_usuario=p.id_usuario,
        id_profesor=p.id_profesor,
        nombres=p.nombres,
        apellidos=p.apellidos,
        tipoDocumento=p.tipo_documento,
        documentoIdentidad=p.documento_identidad,
        telefono=p.telefono,
        estado=p.estado,
        email=p.email,
    ) for p in profesores]

@router.get("/acudientes", response_model=List[AcudienteResponse])
def obtener_acudientes(db: Session = Depends(get_db)):
    acudientes = db.query(
        Usuario.id_usuario,
        Usuario.nombres,
        Usuario.apellidos,
        Usuario.email,
        Usuario.tipo_documento,
        Usuario.documento_identidad,
        Usuario.telefono,
        Usuario.estado,
        Acudiente.id_acudiente,
    ).join(
        Acudiente, Usuario.id_usuario == Acudiente.id_usuario
    ).filter(
        Usuario.rol == "acudiente"
    ).all()

    return [AcudienteResponse(
        id_usuario=a.id_usuario,
        id_acudiente=a.id_acudiente,
        nombres=a.nombres,
        apellidos=a.apellidos,
        tipoDocumento=a.tipo_documento,
        documentoIdentidad=a.documento_identidad,
        telefono=a.telefono,
        estado=a.estado,
        email=a.email,
    ) for a in acudientes]

@router.get("/administradores", response_model=List[AdministradorResponse])
def obtener_administradores(db: Session = Depends(get_db)):
    administradores = db.query(
        Usuario.id_usuario,
        Usuario.nombres,
        Usuario.apellidos,
        Usuario.email,
        Usuario.tipo_documento,
        Usuario.documento_identidad,
        Usuario.telefono,
        Usuario.estado,
        Administrador.id_administrador
    ).join(
        Administrador, Usuario.id_usuario == Administrador.id_usuario
    ).filter(
        Usuario.rol == "administrador"
    ).all()

    return [AdministradorResponse(
        id_usuario=a.id_usuario,
        id_administrador=a.id_administrador,
        nombres=a.nombres,
        apellidos=a.apellidos,
        tipoDocumento=a.tipo_documento,
        documentoIdentidad=a.documento_identidad,
        telefono=a.telefono,
        estado=a.estado,
        email=a.email,
    ) for a in administradores]