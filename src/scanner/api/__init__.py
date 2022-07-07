from fastapi import APIRouter

from .currency import router as currency
from .health_check import router as health_check

router = APIRouter()
router.include_router(health_check)
router.include_router(currency)
