import logging

import requests
from common_libs.utils import build_request_headers
from config import SESSION


class Comments:

    def __init__(self):
        self.url = "/comments"

    def get_all_comments(self, app_url, access_token):
        logging.info("Test :: Get All Comments")
        request_headers = build_request_headers(access_token)
        response = SESSION.get(f"{app_url}{self.url}", headers=request_headers)
        logging.debug(response)
        return response

    def create_comment(self, app_url, access_token, message="Hello World!"):
        import uuid
        uid = uuid.uuid4()
        logging.info("Test :: Creating Comments")
        request_header = build_request_headers(access_token)
        params = {
            'text': f'{message}',
        }
        response = SESSION.post(f"{app_url}{self.url}", headers=request_header, params=params)
        logging.debug(response)
        return response
