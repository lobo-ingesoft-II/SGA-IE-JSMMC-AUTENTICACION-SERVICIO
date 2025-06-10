from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+pymysql://uwyl6ydk2wi90jzi:hGdw1dBMo0Fxg78F6Zav@bbfzaofbtbqcke4vwvkh-mysql.services.clever-cloud.com:3306/bbfzaofbtbqcke4vwvkh" # PONER LAS CREDENCIALES QUE COMPARTIO JHOAN 

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()