from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    BOT_TOKEN: str
    DATABASE_URL: str

    model_config = SettingsConfigDict(case_sensitive=True, env_file=".env")

settings = Settings()