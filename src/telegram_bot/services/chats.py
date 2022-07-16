import requests
from loguru import logger

from src.telegram_bot.database.crud import add_data_new_group
from src.telegram_bot.services.exceptions import TelegramGroupError


class ChatsTelegram:
    def __init__(self, url: str, api_key: str):
        self.url = url
        self.api_key = api_key

    def _get_group_id_from_bot(self) -> dict | int:
        response = requests.get(url=self.url.format(self.api_key))

        try:
            response.raise_for_status()

            logger.info(f"Response telegram API: '{response.json()}'")
            return response.json()

        except requests.exceptions.HTTPError as ex:
            logger.error(f"Response telegram API: '{ex.response.text}'")
            return ex.response.status_code

    @staticmethod
    def _search_object_with_chat_id(body: dict) -> list:
        chat_id_list = []

        for result in body.get("result"):
            for kr in result.keys():
                if isinstance(result.get(kr), dict):
                    for k in result.get(kr).keys():
                        if k in ("chat",):
                            chat_id_list.append(result.get(kr).get(k))

        return chat_id_list

    def add_chat_id_to_database(self) -> None:
        bot_response = self._get_group_id_from_bot()

        if bot_response not in (401, 404) and len(bot_response.get("result")) > 0:
            chat_id_list = self._search_object_with_chat_id(bot_response)

            if chat_id_list:
                for item in chat_id_list:
                    try:
                        add_data_new_group(
                            id_chat=item.get("id"),
                            title_chat=item.get("title"),
                            type_chat=item.get("type"),
                        )
                        logger.info(f"Add '{item}' to database")
                    except:
                        logger.info(f"'{item}' Exist to database")

            else:
                raise TelegramGroupError("Unsuccessful attempt to write to database")
        else:
            raise TelegramGroupError(f"API Telegram for bot returned error")
