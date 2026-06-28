from pydantic_settings import BaseSettings,SettingsConfigDict
from functools import lru_cache
from pydantic import Field
import os

class Settings(BaseSettings):

    model_config = SettingsConfigDict(env_file=os.getenv("ENV_FILE",".env"),extra="ignore")
    app_name : str = Field(...,alias="APP_NAME")
    environment : str = Field(...,alias="ENVIRONMENT")
    database_url: str = Field(...,alias="DATABASE_URL")

@lru_cache
def get_settings() -> Settings:
    return Settings
