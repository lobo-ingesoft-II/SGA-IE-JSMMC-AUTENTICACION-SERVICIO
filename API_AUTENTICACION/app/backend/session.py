import mysql.connector
from app.backend.config import settings # Traer el valor de configuración de la URI de MongoDB
from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError



# Configuración de la conexión
config = {
    'host': settings.host_mysql,
    'user': settings.user_mysql,
    'password': settings.password_mysql,
    'database': settings.database_mysql,
    'port': settings.port_mysql
}

# Construir la URL de conexión
SQLALCHEMY_DATABASE_URL = (
    f"mysql+pymysql://{config['user']}:{config['password']}@"
    f"{config['host']}:{config['port']}/{config['database']}"
)


# Crear engine
engine = create_engine(SQLALCHEMY_DATABASE_URL) # Gestiona las conexion en la app

# Crear sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # Crea una sección personalizada cada vez que la base de datos necesita realziar una operacion de CONSULTA, INSERTAR, ACTUALIZAR

# Base declarativa para modelos
Base = declarative_base()  # Es la clase base de la que SE DEBEN HEREDAR todos los modelos o tablas 


# Verificar la conexion 
try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT VERSION()"))
        version = result.fetchone()
        print(f"Conectado a MySQL versión: {version[0]}")
except Exception as e:
    print("Error al conectar a la base de datos:", e)

