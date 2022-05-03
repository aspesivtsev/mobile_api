import pytest
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_attractions_endpoint():
    client = APIClient()
    response = client.get('/api/attractions/')
    print(response.status_code)
    assert response.status_code == 200

@pytest.mark.django_db
def test_attractions_json_format():
    client = APIClient()
    response = client.get('/api/attractions/')
    assert response.headers["Content-Type"] == "application/json"


