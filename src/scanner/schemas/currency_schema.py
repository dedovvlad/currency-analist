from enum import Enum
from typing import Optional

from pydantic import BaseModel


class CurrencyCode(str, Enum):
    USD = "USD"
    EUR = "EUR"


class Currency(BaseModel):
    USD: Optional[float]
    EUR: Optional[float]
