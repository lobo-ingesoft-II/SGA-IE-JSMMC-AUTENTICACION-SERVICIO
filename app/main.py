from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from app.backend.database import try_BD
from app.routers import usuario_routes  # Importar las rutas del archivo de autenticacion 
from app.routers import auth_routes, admin_routes, profesor_routes, acudiente_routes

from app.backend.session import Base, engine

#Lee todas las clases que heredan de Base.
# Genera el SQL necesario para crear las tablas en la base de datos.
# No borra ni modifica tablas existentes, solo crea las que faltan.
Base.metadata.create_all(bind=engine)

# Instancia de FastAPI
app = FastAPI()

# Importar las rutas
app.include_router(usuario_routes.router)
app.include_router(auth_routes.router)
app.include_router(admin_routes.router)
app.include_router(profesor_routes.router)
app.include_router(acudiente_routes.router)



# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas las orígenes
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos HTTP
    allow_headers=["*"],  # Permitir todos los encabezados
)

# if __name__ == '__main__':
#     app.run(debug=True)