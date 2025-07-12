# tests/test_auth.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.services.auth_utils import get_password_hash
from app.models.usuario_model import Usuario
from app.backend.database import get_db  # 👈 necesario para override correcto

client = TestClient(app)

# Simulación de resultados de consulta
class FakeQueryResult:
    def __init__(self, result):
        self._result = result

    def filter(self, *_):
        return self

    def first(self):
        return self._result

# Simulación de la base de datos
class FakeDB:
    def __init__(self, usuario=None):
        self.usuario = usuario

    def query(self, modelo):
        if modelo == Usuario:
            return FakeQueryResult(self.usuario)
        return FakeQueryResult(None)

# ✅ Test: login exitoso
def test_login_exitoso():
    usuario = Usuario(
        id_usuario=1,
        email="test@example.com",
        contrasena_hash=get_password_hash("password123"),
        rol="profesor",
        nombres="Juan",
        apellidos="Pérez"
    )
    fake_db = FakeDB(usuario)
    app.dependency_overrides[get_db] = lambda: fake_db

    response = client.post("/auth/login", json={
        "email": "test@example.com",
        "contrasena": "password123"
    })

    assert response.status_code == 200
    json = response.json()
    assert "access_token" in json
    assert json["rol"] == "profesor"

# ❌ Test: email no registrado
def test_login_email_invalido():
    fake_db = FakeDB(None)
    app.dependency_overrides[get_db] = lambda: fake_db

    response = client.post("/auth/login", json={
        "email": "desconocido@example.com",
        "contrasena": "password123"
    })

    assert response.status_code == 400
    assert response.json()["detail"] == "Email no registrado"

# ❌ Test: contraseña incorrecta
def test_login_contrasena_incorrecta():
    usuario = Usuario(
        id_usuario=1,
        email="test@example.com",
        contrasena_hash=get_password_hash("otra_clave"),
        rol="profesor",
        nombres="Juan",
        apellidos="Pérez"
    )
    fake_db = FakeDB(usuario)
    app.dependency_overrides[get_db] = lambda: fake_db

    response = client.post("/auth/login", json={
        "email": "test@example.com",
        "contrasena": "password123"
    })

    assert response.status_code == 400
    assert response.json()["detail"] == "Error en la verificación de contraseña"




