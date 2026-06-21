from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    APP_NAME: str = "TeleBoost AI"
    APP_VERSION: str = "3.0.0"
    DEBUG: bool = True
    SECRET_KEY: str = "change-me-in-production"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440

    DATABASE_URL: str = "sqlite+aiosqlite:///./teleboost.db"
    REDIS_URL: str = "redis://localhost:6379"

    CORS_ORIGINS: List[str] = ["*"]

    TELEGRAM_BOT_TOKEN: str = ""
    TELEGRAM_WEBAPP_URL: str = "https://teleboostai.ru"

    GPT_API_KEY: str = ""
    GPT_MODEL: str = "gpt-4o"
    CEREBRAS_API_KEY: str = ""

    PROXY_DEFAULT_TYPE: str = "socks5"

    class Config:
        env_file = ".env"

settings = Settings()
