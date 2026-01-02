import os
from dataclasses import dataclass


@dataclass(frozen=True)
class ClickHouseConfig:
    host: str
    database: str
    user: str = "default"
    password: str = ""



def get_clickhouse_config() -> ClickHouseConfig:
    return ClickHouseConfig(
        host=os.getenv("CLICKHOUSE_HOST", "http://clickhouse:8123"),
        database=os.getenv("CLICKHOUSE_DB", "churn"),
    )


def pandahouse_connection(cfg: ClickHouseConfig) -> dict:
    return {
        "host": cfg.host,
        "database": cfg.database,
        "user": cfg.user,
        "password": cfg.password,
    }
