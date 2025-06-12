from app.backend.session import SessionLocal
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import text


def get_db():
    db = SessionLocal()

    # Utilizacion de Yield: Cuando FastAPI dectecta que se esta usando Yield entonces sabe que al finalizar el request debe cerrar la sesión automaticamente
    try:
        yield db
    finally:
        db.close()  # Se ejecuta siempre al final y libera el recurso Y EL RECURSO DEBE DE SER LIBERADO 



def try_BD():
    try:
        db = SessionLocal()
        result = db.execute(text("SELECT VERSION();"))
        version = result.fetchone()
        print(f"Conexión exitosa. Versión de MySQL: {version[0]}")
    except SQLAlchemyError as e:
        print("Error al conectar a la base de datos:", e)
    finally:
        db.close()  # Muy importante cerrar la conexión