from pathlib import Path
from pydantic import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

env_path = Path(__file__).parent / ".env"

class Settings(BaseSettings):
    database_url: PostgresDsn
    secret_key: str
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    model_config = SettingsConfigDict(env_file=env_path,  env_file_encoding="utf-8",)

@lru_cache()
def get_settings():
    return Settings()

settings = get_settings()