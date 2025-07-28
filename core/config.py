from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel, PostgresDsn


class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000
    reload: bool = True


class AppConfig(BaseModel):
    title: str = "FastAPI Skeleton"
    version: str = "1.0.0"
    description: str = "FastAPI Skeleton"
    summary: str = "FastAPI Skeleton"


class ApiPrefixConfig(BaseModel):
    prefix: str = "/api"
    products: str = "/products"
    users: str = "/users"


class JWTSettings(BaseModel):
    secret_key: str = "secret"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 15


class DatabaseConfig(BaseModel):
    url: PostgresDsn
    echo: bool
    max_overflow: int = 10
    pool_size: int = 50
    echo_pool: bool = False


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".env"),
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="APP_CONFIG__",
        extra="ignore",
    )

    app: AppConfig = AppConfig()
    run: RunConfig = RunConfig()
    api: ApiPrefixConfig = ApiPrefixConfig()

    jwt: JWTSettings = JWTSettings()
    db: DatabaseConfig


settings = Settings()
# print(settings)