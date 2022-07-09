import os

from dotenv import load_dotenv

load_dotenv()

env = os.environ.get

# UVICORN
SERVER_HOST = env("SERVER_HOST", "")
SERVER_PORT = env("SERVER_PORT", "")

# BANKI.RU
URL_BANKI_RU = env(
    "URL_BANKI_RU", "https://www.banki.ru/products/currency/ajax/quotations/value/cbr/"
)

# REDIS
REDIS_HOST = env("REDIS_HOST", "")
REDIS_PORT = env("REDIS_PORT", "")
TIME_CACHE = env("TIME_CACHE", 60)
