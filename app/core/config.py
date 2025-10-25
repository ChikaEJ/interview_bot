from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    BOT_TOKEN: str
    DATABASE_URL: str
    REDIS_PORT: int
    REDIS_HOST: str
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    OPENAI_API_KEY: str

    model_config = SettingsConfigDict(case_sensitive=True, env_file=".env")

settings = Settings()