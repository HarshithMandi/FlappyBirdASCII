from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    APP_NAME: str
    DEBUG: bool = False

    class Config:
        env_file = ".env"

settings = Settings()