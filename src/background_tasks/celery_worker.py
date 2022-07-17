from celery import Celery

import settings
from src.telegram_bot.services.chats import ChatsTelegram
from src.telegram_bot.services.message import MessageTelegram

celery = Celery(
    namespace="CELERY",
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND,
)


@celery.task(name="update_chat_id_table")
def update_chat_id_table():
    chats = ChatsTelegram(
        url=settings.URL_API_BOT_DATA,
        api_key=settings.BOT_API_KEY,
    )
    chats.add_chat_id_to_database()


@celery.task(name="send_to_telegram")
def send_to_telegram():
    message = MessageTelegram(
        url=settings.URL_API_BOT_MESSAGE,
        api_key=settings.BOT_API_KEY,
    )
    message.send_messadge_for_groups()


celery.conf.beat_schedule = {
    "update_chat_id_table": {
        "task": "update_chat_id_table",
        "schedule": settings.CELERY_TIME_SLEEP,
    },
    "send_to_telegram": {
        "task": "send_to_telegram",
        "schedule": settings.CELERY_TIME_SLEEP,
    },
}
