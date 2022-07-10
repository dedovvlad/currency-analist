from celery import Celery

import settings
from telegram_bot.services.bot import send_message_to_telegram_chat

celery = Celery(__name__)

celery.conf.broker_url = settings.CELERY_BROKER_URL
celery.conf.result_backend = settings.CELERY_RESULT_BACKEND


@celery.task(name="send_to_telegram")
def send_to_telegram():
    send_message_to_telegram_chat()


celery.conf.beat_schedule = {
    "something-task-every-ten-seconds": {
        "task": "send_to_telegram",
        "schedule": settings.CELERY_TIME_SLEEP
    }
}
