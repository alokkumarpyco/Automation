import requests
import logging
import re
import os

SESSION = requests.Session()

APP_URL = "http://localhost:8080"
ADMIN_USER = "admin"
ADMIN_PASSWD = "admin"


LOG = logging.getLogger()


class HideSensitiveData(logging.Filter):

    def filter(self, record):
        record.msg = str(record.msg).replace(ADMIN_PASSWD, "*******")
        record.msg = re.sub(r'Authorization.*?,',
                            'Authorization\': \'*******\', ', str(record.msg))
        return True


LOG.addFilter(HideSensitiveData())