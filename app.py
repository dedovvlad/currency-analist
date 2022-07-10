import uvicorn
from fastapi import FastAPI

from src.scanner.api import router
from src import settings

app = FastAPI()
app.include_router(router)


if __name__ == "__main__":
    uvicorn.run(
        app=app,
        host=settings.SERVER_HOST,
        port=settings.SERVER_PORT,
    )
