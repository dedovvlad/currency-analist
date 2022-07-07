from enum import Enum

from pydantic import BaseModel


class CurrencyCode(str, Enum):
    USD = "USD"
    EUR = "EUR"


class Currency(BaseModel):
    USD: float
    EUR: float
