import logging.config
from app.common.log_config import LOGGING_CONFIG
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from starlette.middleware.cors import CORSMiddleware

from app.components.health.router import health_router
from app.components.knapsack.router import knapsack_router
from app.database.database import create_db_and_tables, engine
from app.database.models import Task
from app.dependencies import Dependencies


@asynccontextmanager
async def _app_lifespan(_: FastAPI) -> AsyncGenerator[None, None]:
    """
    Governs startup & shutdown of the app as recommended

    Args:
        _: the FastAPI app
    """
    logging.info("Initiating dependencies...")
    Dependencies.start()
    create_db_and_tables()
    logging.info("Done initiating dependencies.")

    yield

    logging.info("Closing connections to DB & cache...")
    await Dependencies.stop()


def create_app() -> FastAPI:
    """
    Creates FastAPI app instance.
    Mounts routers, and adds a root endpoint.
    """

    # Setup Logs
    logging.config.dictConfig(LOGGING_CONFIG)

    # Create API
    app = FastAPI(title="XXXX", version="1.0.0", lifespan=_app_lifespan)

    # Middleware
    app.add_middleware(
        CORSMiddleware,  # type: ignore
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Apply Routers
    app.include_router(health_router, prefix="/health")
    app.include_router(knapsack_router, prefix="/knapsack")

    @app.get("/", response_class=PlainTextResponse)
    async def get_root():
        return "Root ..."

    return app
