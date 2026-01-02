import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    clickhouse_host: str = "clickhouse"
    model_name: str = "churn_model"
    model_stage: str = "Production"
    model_version: str = "1.0.0"

    class Config:
        env_prefix = ""
        case_sensitive = False


settings = Settings()
