from celery import Celery
from src import settings

celery = Celery(__name__)

celery.conf.broker_url = settings.CELERY_BROKER_URL
celery.conf.result_backend = settings.CELERY_RESULT_BACKEND


@celery.task(name="check")
def check():
    print('I am checking your stuff')


celery.conf.beat_schedule = {
    "run-me-every-ten-seconds": {
    "task": "check",
    "schedule": 10.0
    }
}

# celery -A celery_worker.celery beat --loglevel=info
# celery -A celery_worker.celery worker --loglevel=info