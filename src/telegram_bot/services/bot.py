from typing import Any

import requests

from src.scanner.services.responce_currency import get_currency
from src.telegram_bot.database.crud import add_data_new_group, get_data_groups

CHAT_ID = "-1001551599820"
BOT_API_KEY = "5381914553:AAH155sIqXy_FY_SoZCeH3zVaO-pUTzXpk4"
URL_API_TELEGRAM_SEND_MESSAGE = (
    "https://api.telegram.org/bot{}/sendMessage?chat_id={}&parse_mode=html&text={}"
)
URL_API_TELEGRAM_META_ABOUT_BOT = "https://api.telegram.org/bot{}/getUpdates"


class MessageTelegram:
    pass


def send_messadge_for_groups():
    groups_list = get_data_groups()
    text = "<b>EXCHANGE RATE:</b>\n{}"
    for item in groups_list:
        url = URL_API_TELEGRAM_SEND_MESSAGE.format(
            BOT_API_KEY, item.chat_id, text.format(get_currency())
        )
        requests.get(url)
