import os

env = os.environ.get

# UVICORN
SERVER_HOST = env("SERVER_HOST", "0.0.0.0")
SERVER_PORT = env("SERVER_PORT", 8000)

# BANKI.RU
URL_BANKI_RU = "https://www.banki.ru/products/currency/ajax/quotations/value/cbr/"
