from pydantic import BaseSettings


class SettingsUvicorn(BaseSettings):
    server_host: str = "127.0.0.1"
    server_port: int = 8886


class URLBankiRu(BaseSettings):
    url: str = "https://www.banki.ru/products/currency/ajax/quotations/value/cbr/"


settings = SettingsUvicorn(
    _env_file=".env",
    _env_file_encoding="utf-8",
)

url_banki_ru = URLBankiRu()
