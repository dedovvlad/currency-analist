from celery import Celery

import settings

celery = Celery(__name__)

celery.conf.broker_url = settings.CELERY_BROKER_URL
celery.conf.result_backend = settings.CELERY_RESULT_BACKEND


@celery.task(name="something_task")
def something_task():
    print('I am something task')


celery.conf.beat_schedule = {
    "something-task-every-ten-seconds": {
        "task": "something_task",
        "schedule": settings.CELERY_TIME_SLEEP
    }
}
