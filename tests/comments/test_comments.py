import requests
import pytest
from common.utils import build_request_headers


def test_get_all_comments(login_as_admin):
    request_header = build_request_headers(login_as_admin)
    response = requests.get("http://localhost:8080/comments", headers=request_header)
    print(response.text)
    assert response.ok


def test_get_all_comments_2(login_as_admin):
    for i in range(100):
        access_token = login_as_admin
        print(access_token)
        print()
        request_header = {
            "Authorization": f"Bearer {access_token}",
            "Accept": "application/json"
        }
        response = requests.get("http://localhost:8080/comments", headers=request_header)
        print(response.text)
        assert response.ok
