from settings import BOT_API_KEY, URL_API_BOT_DATA
from src.telegram_bot.services.chats import ChatsTelegram

chat = ChatsTelegram(url=URL_API_BOT_DATA, api_key=BOT_API_KEY)


def test_add_some_item_to_db(requests_mock, response_with_object):
    requests_mock.get(URL_API_BOT_DATA.format(BOT_API_KEY), json=response_with_object)
    chat.add_chat_id_to_database()
