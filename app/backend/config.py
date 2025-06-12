from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    mongo_uri: str = Field(..., alias="MONGO_URI")
    url_api_pre_registro: str = Field(..., alias="SERVIDOR_API_PREMATRICULA_URL")
    host_mysql : str = Field(..., alias="HOST_MYSQL")
    user_mysql : str = Field(..., alias="USER_MYSQL")
    password_mysql : str = Field(..., alias="PASSWORD_MYSQL")
    database_mysql : str = Field(..., alias="DATABASE_MYSQL")
    port_mysql  : str = Field(..., alias="PORT_MYSQL")
    class Config:
        env_file = ".env"
        extra = "allow"

settings = Settings()

