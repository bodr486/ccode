from pydantic_settings import BaseSettings,SettingsConfigDict
from pydantic import root_validator
from dotenv import dotenv_values


class DBconfif(BaseSettings):

    DB_PORT : int
    DB_NAME : str
    DB_PASS : str
    DB_HOST : str
    DB_USER : str

    # model = SettingsConfigDict(env_file='.env')
    model_config = SettingsConfigDict(env_file=".env")

    @property
    def DATABASE_URL(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

class Settings(DBconfif):
    pass

settings = Settings()