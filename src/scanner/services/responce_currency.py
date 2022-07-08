from datetime import datetime

import requests
from loguru import logger

from src.scanner import settings

from .exceptions import CurrencyCalculateError

CURRENCY = {
    "EUR": 978,
    "USD": 840,
}


def get_currency(currency_name: str = None) -> dict:
    """
    Функцию вызывает вью которая отдает уже конечный рещультат
    :param currency_name: буквенный код валюты
    :return: JSON с с буквенным кодом и стоимостью валюты
    """
    currency_dict = dict()
    if currency_name:
        course = __calculate_currency(__get_actual_course(CURRENCY.get(currency_name)))
        currency_dict.update({currency_name: course})
    else:
        for key, value in CURRENCY.items():
            course = __calculate_currency(__get_actual_course(CURRENCY.get(key)))
            currency_dict.update({key: course})

    logger.info(currency_dict)
    return currency_dict


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
