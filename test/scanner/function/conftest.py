import pytest
from fastapi.testclient import TestClient

from src.scanner.app import app


@pytest.fixture(scope="session")
def client() -> TestClient:
    client = TestClient(app)
    return client
