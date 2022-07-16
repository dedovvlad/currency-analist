import pytest


@pytest.fixture()
def response_without_object() -> dict:
    body = {
        "ok": True,
        "result": []
    }
    return body


@pytest.fixture()
def response_without_auth() -> dict:
    body = {
        "ok": False,
        "error_code": 401,
        "description": "Unauthorized"
    }
    return body


@pytest.fixture()
def response_bed_request() -> dict:
    body = {
        "ok": False,
        "error_code": 404,
        "description": "Not Found"
    }
    return body


@pytest.fixture()
def response_with_object() -> dict:
    body = {
        "ok": True,
        "result": [
            {
                "message": {
                    "chat": {
                        "id": -10000,
                        "title": "MVPCurrencyCourse Chat",
                        "type": "supergroup"
                    },
                },
            },
            {
                "my_chat_member": {
                    "chat": {
                        "id": -10001,
                        "title": "MVPCurrencyCourse Chat",
                        "type": "supergroup"
                    },
                },
            },
        ]
    }
    return body
