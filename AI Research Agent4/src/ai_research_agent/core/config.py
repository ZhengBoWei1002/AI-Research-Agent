"""Configuration management for the application."""

from functools import lru_cache
from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    app_name: str = Field(default="AI Research Agent", alias="APP_NAME")
    app_env: str = Field(default="local", alias="APP_ENV")
    app_debug: bool = Field(default=True, alias="APP_DEBUG")
    app_host: str = Field(default="0.0.0.0", alias="APP_HOST")
    app_port: int = Field(default=8000, alias="APP_PORT")
    app_log_level: str = Field(default="INFO", alias="APP_LOG_LEVEL")

    openai_api_base: str = Field(
        default="https://api.openai.com/v1",
        alias="OPENAI_API_BASE",
    )
    openai_api_key: str = Field(default="replace-me", alias="OPENAI_API_KEY")
    openai_model: str = Field(default="gpt-4o-mini", alias="OPENAI_MODEL")
    openai_embedding_model: str = Field(
        default="text-embedding-3-small",
        alias="OPENAI_EMBEDDING_MODEL",
    )

    sqlite_path: Path = Field(default=Path("./data/sqlite/app.db"), alias="SQLITE_PATH")
    chroma_persist_directory: Path = Field(
        default=Path("./data/chroma"),
        alias="CHROMA_PERSIST_DIRECTORY",
    )

    research_max_iterations: int = Field(default=3, alias="RESEARCH_MAX_ITERATIONS")
    research_timeout_seconds: int = Field(default=180, alias="RESEARCH_TIMEOUT_SECONDS")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        populate_by_name=True,
    )


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Return a cached settings object for dependency injection."""

    return Settings()
