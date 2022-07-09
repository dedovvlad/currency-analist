def test_get_healt_check(client):
    """Тест для проверки запроса хелсчека."""
    response = client.get("/health_check")
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}
