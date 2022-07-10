import uvicorn
from fastapi import FastAPI

import settings
from src.scanner.api import router

app = FastAPI()
app.include_router(router)


if __name__ == "__main__":
    uvicorn.run(
        app=app,
        host=settings.SERVER_HOST,
        port=settings.SERVER_PORT,
    )
