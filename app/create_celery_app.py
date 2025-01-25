from celery import Celery
from app.env import SETTINGS


def create_celery_app() -> Celery:
    celery_app = Celery(
        __name__,
        broker=SETTINGS.celery_broker_url,
        backend=SETTINGS.celery_result_backend,
    )

    celery_app.conf.update(
        imports=[
            "app.components.knapsack.celery_tasks"  # path to celery tasks file
        ],
        broker_connection_retry_on_startup=True,
        task_track_started=True,
    )

    return celery_app


celery_app = create_celery_app()
