import uvicorn
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from app.env import SETTINGS
from app.knapsack_router import knapsack

app = FastAPI(title="FastAPI-celery", version="1.0.0")

app.include_router(knapsack.router, prefix="/knapsack")


@app.get("/", response_class=PlainTextResponse)
def get_root():
    return "Root ..."


if __name__ == "__main__":
    # Start server
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=SETTINGS.server_port,
        log_level=SETTINGS.server_log_level,
    )
