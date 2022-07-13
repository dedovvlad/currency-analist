import requests

from src.scanner.services.responce_currency import get_currency
from src.telegram_bot.database.crud import add_data_new_group, get_data_groups

CHAT_ID = "-1001551599820"
BOT_API_KEY = "5499587546:AAHu0QeWVttKM8ZED5wKegdmuJH3Loz7YFg"
URL_API_TELEGRAM_SEND_MESSAGE = (
    "https://api.telegram.org/bot{}/sendMessage?chat_id={}&parse_mode=html&text={}"
)
URL_API_TELEGRAM_META_ABOUT_BOT = "https://api.telegram.org/bot{}/getUpdates"


def update_list_chats():
    url = URL_API_TELEGRAM_META_ABOUT_BOT.format(BOT_API_KEY)
    bot_metadata = requests.get(url)
    list_message: list = bot_metadata.json()["result"]

    try:
        list_message.__len__() != 0
    except IndexError as ex:
        pass
    else:
        for item in list_message:
            if item["message"]["chat"]["id"]:
                try:
                    add_data_new_group(
                        chat=item["message"]["chat"]["id"],
                        update=item["message"]["chat"]["id"],
                    )
                except:
                    continue


def send_messadge_for_groups():
    groups_list = get_data_groups()
    text = "<b>EXCHANGE RATE:</b>\n{}"
    for item in groups_list:
        url = URL_API_TELEGRAM_SEND_MESSAGE.format(
            BOT_API_KEY, item.chat_id, text.format(get_currency())
        )
        requests.get(url)
