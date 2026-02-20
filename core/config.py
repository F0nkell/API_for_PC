import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    API_KEY: str = os.getenv("API_KEY", "default_dev_key")
    HOST: str = os.getenv("HOST", "127.0.0.1")
    PORT: int = int(os.getenv("PORT", 8000))
    WORKSPACE_ROOT: str = os.getenv("WORKSPACE_ROOT", "./")

    class Config:
        env_file = ".env"

settings = Settings()