from settings import BOT_API_KEY, URL_API_BOT_DATA
from src.telegram_bot.services.chats import ChatsTelegram

chats_tg = ChatsTelegram(url=URL_API_BOT_DATA, api_key=BOT_API_KEY)


def test_get_response_with_chat_id_list(response_with_object):
    response = chats_tg._search_object_with_chat_id(response_with_object)
    assert isinstance(response, list)
    assert len(response) > 0
    for item in response:
        assert "id" in item.keys()


def test_get_with_empty_list(response_without_object):
    response = chats_tg._search_object_with_chat_id(response_without_object)
    assert isinstance(response, list)
    assert len(response) == 0
