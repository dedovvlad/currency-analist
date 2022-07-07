from random import choice

import pytest

from src.scanner.services.responce_currency import (
    CURRENCY,
    __calculate_currency,
    __get_actual_course,
    get_currency,
)


@pytest.mark.parametrize(
    "input_dict, output_float",
    [
        ({"value": 56, "ratio": 1}, 56.0),
        ({"value": 11.8, "ratio": 100}, 0.118),
        ({"value": 100, "ratio": 100}, 1.0),
    ],
)
def test_give_data_positive(input_dict, output_float):
    """
    Тест на проверку калькулятора, как считает валюту,
    стоимостью больше 1 рубля и меньше.
    """
    assert __calculate_currency(input_dict) == output_float


def test_send_banki_ru_positive():
    """
    Тест на проверку метода который отправляет запрос в банки.ру.
    А так же, что присылает словарь и необходимые поля в нем.
    """
    response = __get_actual_course(840)
    assert isinstance(response, dict)
    assert "value" in response
    assert "ratio" in response


@pytest.mark.parametrize("input_atr, output_atr", [("EUR", float)])
def test_get_eur_course_positive(input_atr, output_atr):
    """
    Тест на проверку получения конечного ответа.
    Проверяет, если передать определенные идентификатор валюты.
    """
    assert len(get_currency(input_atr)) > 0
    assert isinstance(get_currency(input_atr), dict)
    assert isinstance(get_currency(input_atr).get(input_atr), output_atr)


@pytest.mark.parametrize("input_atr, output_atr", [(None, float)])
def test_get_some_course_positive(input_atr, output_atr):
    """
    Тест на проверку получения конечного ответа.
    Проверяет, если не передавать идентификатор валюты.
    """
    response = get_currency(input_atr)
    assert len(response) > 1
    assert choice(list(CURRENCY.keys())) in response
    assert isinstance(response.get(choice(list(CURRENCY.keys()))), output_atr)
