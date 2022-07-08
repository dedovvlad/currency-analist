import os

from pydantic import BaseSettings

env = os.environ.get

# UVICORN
SERVER_HOST = env("SERVER_HOST", "0.0.0.0")
SERVER_PORT = env("SERVER_PORT", 8000)

# BANKI.RU
URL_BANKI_RU = "https://www.banki.ru/products/currency/ajax/quotations/value/cbr/"


# class SettingsUvicorn(BaseSettings):
#     server_host: str = "0.0.0.0"
#     server_port: int = 8000


class URLBankiRu(BaseSettings):
    url: str = "https://www.banki.ru/products/currency/ajax/quotations/value/cbr/"


# settings = SettingsUvicorn(
#     _env_file=".env",
#     _env_file_encoding="utf-8",
# )

url_banki_ru = URLBankiRu()
