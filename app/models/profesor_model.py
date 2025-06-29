from sqlalchemy import Column, Integer, String, Boolean
from app.backend.session import Base

class Profesor(Base):
    __tablename__ = "profesores"

    id_profesor = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, nullable=False, unique=True)
    especialidad = Column(String(100))
    es_director = Column(Boolean, nullable=False, default=False)
