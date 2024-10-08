from dotenv import find_dotenv, load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    MODE: str

    DB_NAME: str
    DB_USER: str
    DB_PASS: str
    DB_HOST: str
    DB_PORT: str
    DB_NAME_SCHEDULER: str

    REDIS_HOST: str
    REDIS_PORT: str

    @property
    def DB_URL(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def DB_URL_SCHEDULER(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME_SCHEDULER}"

    model_config = SettingsConfigDict(env_file=".env")


load_dotenv(find_dotenv(".env"))
settings = Settings()

SITE_URL = "https://spimex.com/markets/oil_products/trades/results/"
SITE_DOMAIN = "https://spimex.com"
