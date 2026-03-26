from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


_DEFAULT_BASE_DIR = Path(__file__).resolve().parents[2]
_DEFAULT_DB_PATH = (_DEFAULT_BASE_DIR / "hiring.db").resolve()
_DEFAULT_DB_URL = f"sqlite:///{_DEFAULT_DB_PATH.as_posix()}"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="HIRING_", env_file=".env", case_sensitive=False)

    # Default SQLite DB lives at: <repo>/hiring_app/hiring.db
    database_url: str = _DEFAULT_DB_URL


settings = Settings()
