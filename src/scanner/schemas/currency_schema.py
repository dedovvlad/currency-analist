from enum import Enum
from typing import Optional

from pydantic import BaseModel


class CurrencyCode(str, Enum):
    USD: Optional = "USD"
    EUR: Optional = "EUR"


class Currency(BaseModel):
    USD: float
    EUR: float
