from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="HIRING_", env_file=".env", case_sensitive=False)

    database_url: str = "sqlite:///./hiring.db"


settings = Settings()
