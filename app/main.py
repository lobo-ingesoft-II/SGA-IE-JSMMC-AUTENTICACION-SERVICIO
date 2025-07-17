from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from app.backend.database import try_BD
from app.routers import usuario_routes  # Importar las rutas del archivo de autenticacion 
from app.routers import auth_routes, admin_routes, profesor_routes, acudiente_routes

from app.backend.session import Base, engine

from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
from starlette.responses import Response
from app.observability.metrics import REQUEST_COUNT, REQUEST_LATENCY, ERROR_COUNT
import time
from fastapi import Request

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

@app.middleware("http")
async def metrics_middleware(request: Request, call_next):
    start_time = time.time()
    try:
        response = await call_next(request)
        status = response.status_code
    except Exception:
        status = 500
        raise
    finally:
        latency = time.time() - start_time
        method = request.method
        endpoint = request.url.path

        REQUEST_COUNT.labels(method=method, endpoint=endpoint).inc()
        REQUEST_LATENCY.labels(method=method, endpoint=endpoint).observe(latency)
        if status >= 400:
            ERROR_COUNT.labels(method=method, endpoint=endpoint, status_code=str(status)).inc()

    return response

@app.get("/metrics")
def metrics():
    return Response(content=generate_latest(), media_type=CONTENT_TYPE_LATEST)

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