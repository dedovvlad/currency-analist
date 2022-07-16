from src.telegram_bot.services.chats import ChatsTelegram
from settings import BOT_API_KEY, URL_API_BOT_DATA


chat = ChatsTelegram(url=URL_API_BOT_DATA, api_key=BOT_API_KEY)


def test_response_from_tg_with_one_group_id(requests_mock, response_with_object):
    """
    Тест на проверку запроса в ТГ и ответа с нужным 1 объектом.
    Ожидается словарь с ID группы.
    """
    requests_mock.get(URL_API_BOT_DATA.format(BOT_API_KEY), json=response_with_object)
    get_chat = chat._get_group_id_from_bot()
    assert isinstance(get_chat, dict)
    assert len(get_chat.get("result")) == len(response_with_object.get("result"))


def test_response_from_tg_without_any_objects(requests_mock, response_without_object):
    """
    Тест на проверку запроса в ТГ и ответа если объект result пуст.
    Ожидается исключение и соответсвующий текст.
    """
    requests_mock.get(URL_API_BOT_DATA.format(BOT_API_KEY), json=response_without_object)
    get_chat = chat._get_group_id_from_bot()
    assert isinstance(get_chat, dict)
    assert len(get_chat.get("result")) == 0


def test_response_not_auth(requests_mock, response_without_auth):
    """
    Тест на проверку запроса в ТГ и ответа если API KEY невалидный.
    Ожидается исключение и соответсвующий текст.
    """
    requests_mock.get(URL_API_BOT_DATA.format(BOT_API_KEY), json=response_without_auth, status_code=401)
    get_chat = chat._get_group_id_from_bot()
    assert get_chat == 401


def test_response_bed_request(requests_mock, response_bed_request):
    """
    Тест на проверку запроса в ТГ и ответа если плохой запрос.
    Ожидается исключение и соответсвующий текст.
    """
    requests_mock.get(URL_API_BOT_DATA.format(BOT_API_KEY), json=response_bed_request, status_code=404)
    get_chat = chat._get_group_id_from_bot()
    assert get_chat == 404
