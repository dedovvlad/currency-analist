import uvicorn
from fastapi import FastAPI

from src.scanner.api import router
from src.scanner.settings import settings

app = FastAPI()
app.include_router(router)


if __name__ == "__main__":
    uvicorn.run(
        app=app,
        host=settings.server_host,
        port=settings.server_port,
    )
