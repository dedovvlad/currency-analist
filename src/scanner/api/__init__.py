from fastapi import APIRouter
from .health_check import router as health_check
from .currency import router as currency

router = APIRouter()
router.include_router(health_check)
router.include_router(currency)
