from typing import Annotated, Literal
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Environment Settings
    env: Literal["local", "test", "dev", "prod"] = "local"
    debug: bool = False

    # Server configuration
    server_port: int = 8080
    server_log_level: str = "info"

    # Database configuration
    db_user: str = ""
    db_password: str = ""
    db_name: str = ""
    db_host: str = ""
    db_url: str = ""
    sqlmodel_url: str = ""

    # Celery
    celery_log_level: str = "INFO"
    celery_log_file_path: str = "/tmp/celery.txt"
    celery_broker_url: str = ""
    celery_result_backend: str = ""
    # celery_result_backend: str = f"redis://redis:6379/0"


SETTINGS = Settings()
