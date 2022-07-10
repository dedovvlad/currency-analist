import requests

from src.scanner.services.responce_currency import get_currency

CHAT_ID = "-1001551599820"
BOT_API_KEY = "5499587546:AAHu0QeWVttKM8ZED5wKegdmuJH3Loz7YFg"
URL_API_TELEGRAM_SEND_MESSAGE = "https://api.telegram.org/bot{}/sendMessage?chat_id={}&parse_mode=html&text={}"
URL_API_TELEGRAM_META_ABOUT_BOT = "https://api.telegram.org/bot{}/getUpdates"


def get_chat_id():
    url = URL_API_TELEGRAM_META_ABOUT_BOT.format(BOT_API_KEY)
    response = requests.get(url)
    set_chat_id = set()
    list_message = response.json()["result"]
    for item in list_message:
        if item.get("message"):
            chat_meta = item.get("message")
            if chat_meta.get("chat"):
                set_chat_id.add(str(chat_meta.get("chat").get("id")))

    return set_chat_id


def send_message_to_telegram_chat():
    text = "<b>EXCHANGE RATE:</b>\n{}"
    for id_chat in get_chat_id():
        url = URL_API_TELEGRAM_SEND_MESSAGE.format(BOT_API_KEY, id_chat, text.format(get_currency()))
        requests.get(url)


send_message_to_telegram_chat()
