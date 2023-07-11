import requests
from common_libs.utils import build_request_headers
from config import SESSION


class Comments:

    def __init__(self):
        self.url = "/comments"

    def get_all_comments(self, app_url, access_token):
        request_headers = build_request_headers(access_token)
        response = SESSION.get(f"{app_url}{self.url}", headers=request_headers)
        return response

