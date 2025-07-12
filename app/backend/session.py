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

print(config)
# Construir la URL de conexión




# Crear engine
# engine = create_engine(settings.sqlalchemy_database_uri) # Gestiona las conexion en la app
# DATABASE_URL="mysql+pymysql://root:1234@127.0.0.1:3306/bcj9asygzv10rjmwhyss"

DATABASE_URL="mysql+pymysql://root:@localhost:3306/auth_db"
engine = create_engine(DATABASE_URL) # Gestiona las conexion en la app

# Crear sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # Crea una sección personalizada cada vez que la base de datos necesita realziar una operacion de CONSULTA, INSERTAR, ACTUALIZAR

# Base declarativa para modelos
Base = declarative_base()  # Es la clase base de la que SE DEBEN HEREDAR todos los modelos o tablas 


