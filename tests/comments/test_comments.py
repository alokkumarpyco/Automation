import requests
import pytest
from common_libs.utils import build_request_headers
from common_libs.comments import Comments
from config import APP_URL
import logging


# from common_libs.utils import build_request_headers

def test_get_all_comments(login_as_admin):
    response = Comments().get_all_comments(f"{APP_URL}", login_as_admin)
    logging.info("Test of Logging")
    assert response.ok


def stest_ui():
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By

    driver = webdriver.Firefox()
    driver.get("http://www.python.org")
    assert "Python" in driver.title
    elem = driver.find_element(By.NAME, "q")
    elem.clear()
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
    driver.close()
