from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="LMS_", env_file=".env", case_sensitive=False)

    database_url: str = "postgresql+psycopg2://postgres:postgres@localhost:5432/banking_lms"
    allowed_origins: list[str] = ["*"]


settings = Settings()
