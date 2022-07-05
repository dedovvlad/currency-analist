from fastapi import APIRouter
from src.scanner.services.responce_currency import get_currency

router = APIRouter(
    prefix="/currency"
)


@router.get("/actual")
def get_actual_urrency():
    return get_currency()
