import requests
from loguru import logger

from src.scanner.services.responce_currency import get_currency
from src.telegram_bot.database.crud import get_data_groups


class MessageTelegram:
    def __init__(self, url: str, api_key: str):
        self.url = url
        self.api_key = api_key

    @staticmethod
    def _create_message():
        return "<b>EXCHANGE RATE:</b>\n{}"

    def send_messadge_for_groups(self):

        groups_list = get_data_groups()

        for item in groups_list:

            url = self.url.format(
                self.api_key, item.id_chat, self._create_message().format(get_currency())
            )

            try:
                response = requests.get(url)
                response.raise_for_status()
                logger.info(f"Send message for client {item.id_chat}")

            except requests.exceptions.HTTPError as ex:
                logger.error("Error")
