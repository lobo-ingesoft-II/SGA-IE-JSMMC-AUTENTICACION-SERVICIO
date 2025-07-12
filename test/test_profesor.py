import pytest
from fastapi.testclient import TestClient
from app.main import app  # Asegúrate de que app esté importable
from app.models.profesor_model import Profesor
from app.models.usuario_model import Usuario as UsuarioModel
from app.backend.database import get_db

# Cliente de prueba
client = TestClient(app)

# Simulación de base de datos (muy simplificada)
class FakeDB:
    def __init__(self, profesores=None, usuarios=None):
        self._profesores = profesores or []
        self._usuarios = usuarios or []

    def query(self, modelo):
        if modelo.__name__ == "Profesor":
            return FakeQuery(self._profesores)
        elif modelo.__name__ == "Usuario":
            return FakeQuery(self._usuarios)
        return FakeQuery([])

    def close(self):
        pass

    def commit(self):
        pass

    def add(self, obj):
        self._profesores.append(obj)

class FakeQuery:
    def __init__(self, data):
        self._data = data

    def filter(self, condition):
        # Condición simulada
        return self

    def first(self):
        return self._data[0] if self._data else None

    def all(self):
        return self._data


@pytest.fixture
def profesor_y_usuario():
    profesor = Profesor(
        id_profesor=1,
        id_usuario=10,
        especialidad="Matemáticas",
        es_director=True
    )
    usuario = UsuarioModel(
        id_usuario=10,
        nombres="Ana",
        apellidos="Gómez",
        tipo_documento="CC",
        documento_identidad="12345678",
        telefono="1234567890",
        email="ana@example.com",
        rol="profesor",
        estado=True,
        fecha_creacion="2024-01-01T00:00:00",
        fecha_modificacion="2024-01-01T00:00:00"
    )
    return profesor, usuario


# Prueba de /profesor/{id_profesor}
def test_get_profesor_exitoso(profesor_y_usuario):
    profesor, _ = profesor_y_usuario
    fake_db = FakeDB(profesores=[profesor])

    app.dependency_overrides[get_db] = lambda: fake_db
    response = client.get("/profesor/1")
    assert response.status_code == 200
    assert response.json()["id_profesor"] == 1


# Prueba de /profesores/{id_profesor} (profesor + usuario)
def test_get_profesor_completo_exitoso(profesor_y_usuario):
    profesor, usuario = profesor_y_usuario
    fake_db = FakeDB(profesores=[profesor], usuarios=[usuario])

    app.dependency_overrides[get_db] = lambda: fake_db
    response = client.get("/profesor/profesores/1")
    assert response.status_code == 200
    assert response.json()["email"] == "ana@example.com"
    assert response.json()["especialidad"] == "Matemáticas"


# Prueba negativa si no existe el profesor
def test_get_profesor_no_existe():
    fake_db = FakeDB()
    app.dependency_overrides[get_db] = lambda: fake_db

    response = client.get("/profesor/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Profesor no encontrado"
