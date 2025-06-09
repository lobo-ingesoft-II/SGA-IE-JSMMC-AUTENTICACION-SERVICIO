from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.backend.database import try_BD
from app.routers import autentication_routes  # Importar las rutas del archivo de autenticacion 


# Instancia de FastAPI
app = FastAPI()

# Importar las rutas
app.include_router(autentication_routes.router)

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