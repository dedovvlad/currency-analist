import json
from datetime import datetime

import requests
from loguru import logger

import settings

from .exceptions import CurrencyCalculateError

from src.utils.redis_database import Redis

CURRENCY = {
    "EUR": 978,
    "USD": 840,
}

redis_client = Redis(
    redis_host=settings.REDIS_HOST,
    redis_port=settings.REDIS_PORT,
    brunch=("Currency", "EUR",),
)


def get_currency(currency_name: str = None) -> dict:
    """
    Функцию вызывает вью которая отдает уже конечный рещультат
    :param currency_name: буквенный код валюты
    :return: JSON с с буквенным кодом и стоимостью валюты
    """

    # TODO: Убрать костыль с присвоением ключа в кеше
    if currency_name:
        key_redis = currency_name
    else:
        key_redis = "CURRENCY"

    redis_db = redis_client.get_item(key_redis)
    # redis_db = get_item_from_redis(key_redis)
    if not redis_db:
        currency_dict = dict()

        # TODO: Переделать условия и использовать не мок валюты, а эндпоинт
        if currency_name:
            course = __calculate_currency(__get_actual_course(CURRENCY.get(currency_name)))
            currency_dict.update({currency_name: course})
        else:
            for key, value in CURRENCY.items():
                course = __calculate_currency(__get_actual_course(CURRENCY.get(key)))
                currency_dict.update({key: course})

        logger.info(f"Request was from API, {currency_dict}")

        redis_client.setex_item(key=key_redis, item=currency_dict)
        # setex_item_to_redis(key=key_redis, item=currency_dict)
        return currency_dict
    else:
        logger.info(f"Request was from Cache, {json.loads(redis_db)}")
        return json.loads(redis_db)


def __calculate_currency(dict_asis: dict) -> float:
    """
    Функция калькулятор для подсчета стоимости валюты по соотношению к рублю
    :param dict_asis: передается JSON как пришел от api banki.ru
    :return: отдается float значение со стоимостью валюты
    """
    try:
        calculate_currency = float("{:.3f}".format(dict_asis.get("value") / dict_asis.get("ratio")))

    except Exception as ex:
        logger.error("Переданы некорректные данные")
        raise CurrencyCalculateError(error_msg=f"{ex}")

    else:
        return calculate_currency


def __get_actual_course(id_currency: int) -> dict:
    """
    Запрос в banki.ru для получения актуальной стоимости валюты по соотношению к рублю
    :param id_currency: код валюты
    :return: отдается JSON как есть из api
    """
    actual_course = requests.post(
        url=settings.URL_BANKI_RU,
        headers={"X-Requested-With": "XMLHttpRequest"},
        json={"currency_id": id_currency, "date": datetime.timestamp(datetime.now())},
    )
    return actual_course.json()
