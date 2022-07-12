from celery import Celery

import settings
from src.telegram_bot.services.bot import update_list_chats, send_messadge_for_groups

celery = Celery(__name__)

celery.conf.broker_url = settings.CELERY_BROKER_URL
celery.conf.result_backend = settings.CELERY_RESULT_BACKEND


@celery.task(name="update_chat_id_table")
def send_to_telegram():
    update_list_chats()


@celery.task(name="send_to_telegram")
def send_to_telegram():
    send_messadge_for_groups()


celery.conf.beat_schedule = {
    "update_chat_id_table": {
        "task": "update_chat_id_table",
        "schedule": settings.CELERY_TIME_SLEEP
    }
}

celery.conf.beat_schedule = {
    "send_to_telegram": {
        "task": "send_to_telegram",
        "schedule": settings.CELERY_TIME_SLEEP
    }
}
