from fastapi import FastAPI
from app.routers import auth, admin, estudiante, profesor, acudiente
from .database import Base, engine
from fastapi.middleware.cors import CORSMiddleware
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(admin.router)
app.include_router(estudiante.router)
app.include_router(profesor.router)
app.include_router(acudiente.router)

# Configura CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # URL de tu frontend React
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "API de Autenticacion y Roles"}