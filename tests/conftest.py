import requests
import pytest


@pytest.fixture(scope="session")
def login_as_admin():
    payload = {"username": "admin", "password": "admin"}
    response = requests.post("http://localhost:8080/auth/login", data=payload)
    assert response.ok

    access_token = response.json()["access_token"]
    yield access_token
