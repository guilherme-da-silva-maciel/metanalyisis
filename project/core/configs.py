from typing import List
from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):
    API_URL_STR = "/api"
    DB_URL:str = f"postgresql+asyncpg://postgres:postgres@localhost:5432/Metanalysis"
    JWT_SECRET:str = 'JddFk6uD1DEK4yh5ri1LUzVkm7FGhrvBMPh8ZLzorDQ'
    ALGORITHM:str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES:int = 10

    DBBaseModel = declarative_base()

    class Config():
        case_sensitive = True


settings:Settings = Settings()
