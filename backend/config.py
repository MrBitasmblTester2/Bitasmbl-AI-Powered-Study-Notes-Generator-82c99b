import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    env: str = os.getenv("APP_ENV", "dev")

settings = Settings()