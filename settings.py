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

# CELERY
CELERY_BROKER_URL = env("CELERY_BROKER_URL", "")
CELERY_RESULT_BACKEND = env("CELERY_RESULT_BACKEND", "")
CELERY_TIME_SLEEP = env("CELERY_TIME_SLEEP", 10)

# POSTGRES
POSTGRES_USER = env("POSTGRES_USER", "")
POSTGRES_PASSWORD = env("POSTGRES_PASSWORD", "")
POSTGRES_NAME = env("POSTGRES_NAME", "")
POSTGRES_HOST = env("POSTGRES_HOST", "")
POSTGRES_PORT = env("POSTGRES_PORT", "")

# TELEGRAM
BOT_API_KEY = env("BOT_API_KEY", "5381914553:AAH155sIqXy_FY_SoZCeH3zVaO-pUTzXpk4")
URL_API_BOT_DATA = env("URL_API_BOT_DATA", "https://api.telegram.org/bot{}/getUpdates")
URL_API_BOT_MESSAGE = env("URL_API_BOT_MESSAGE", "https://api.telegram.org/bot{}/sendMessage?chat_id={}&parse_mode=html&text={}")
