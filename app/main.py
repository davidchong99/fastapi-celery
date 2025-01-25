import logging
import uvicorn

from app.create_app import create_app
from app.env import SETTINGS


# Create app
app = create_app()

if __name__ == "__main__":
    # Start server
    logging.info(f"Server Log Level: {SETTINGS.server_log_level}")
    logging.info(f"sqlmodel_url : {SETTINGS.sqlmodel_url}")
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=SETTINGS.server_port,
        log_level=SETTINGS.server_log_level,
    )
