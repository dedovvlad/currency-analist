from src.telegram_bot.database.crud import get_data_groups
from src.scanner.services.responce_currency import get_currency
import requests


class MessageTelegram:
    def __init__(self, url: str, api_key: str):
        self.url = url
        self.api_key = api_key

    def send_messadge_for_groups(self):
        groups_list = get_data_groups()
        text = "<b>EXCHANGE RATE:</b>\n{}"
        for item in groups_list:
            url = self.url.format(
                self.api_key, item.chat_id, text.format(get_currency())
            )
            requests.get(url)
