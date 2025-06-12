from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    host_mysql : str = Field(..., alias="HOST_MYSQL")
    user_mysql : str = Field(..., alias="USER_MYSQL")
    password_mysql : str = Field(..., alias="PASSWORD_MYSQL")
    database_mysql : str = Field(..., alias="DATABASE_MYSQL")
    port_mysql  : str = Field(..., alias="PORT_MYSQL")

    @property
    def sqlalchemy_database_uri(self):
        return (
            f"mysql+pymysql://{self.user_mysql}:{self.password_mysql}"
            f"@{self.host_mysql}:{self.port_mysql}/{self.database_mysql}"
        )
    
    
    class Config:
        env_file = ".env"
        extra = "allow"

settings = Settings()

