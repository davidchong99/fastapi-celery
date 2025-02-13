from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Server configuration
    server_port: int = 8080
    server_log_level: str = "info"

    # Database configuration
    db_url: str = ""

    # Celery
    celery_broker_url: str = ""
    celery_result_backend: str = ""


SETTINGS = Settings()
