from fastapi import APIRouter
from scanner.services.responce_currency import get_currency

router = APIRouter(
    prefix="/currency"
)


@router.get("/actual")
def get_actual_urrency():
    return get_currency()
