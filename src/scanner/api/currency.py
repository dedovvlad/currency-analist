from fastapi import APIRouter

from src.scanner.schemas.currency_schema import Currency, CurrencyCode
from src.scanner.services.responce_currency import get_currency

router = APIRouter(prefix="/currency")


@router.get("/actual/", response_model=Currency)
def get_actual_currency(currency_code: CurrencyCode = None):
    return get_currency(currency_code)
