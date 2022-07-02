from fastapi import APIRouter

router = APIRouter()


@router.get("/health_check")
def get_health_check():
    return {"status": "OK"}
