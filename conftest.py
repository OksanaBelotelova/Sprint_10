import pytest
from selenium import webdriver
from data import URLs

@pytest.fixture
def driver():
    url = URLs.base_url
    driver = webdriver.Chrome()
    driver.get(url)
    yield driver
    driver.quit()