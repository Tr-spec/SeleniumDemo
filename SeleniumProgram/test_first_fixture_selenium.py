
import pytest
from selenium import webdriver

driver = None


@pytest.fixture
def setup():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield
    print(driver.title)
    driver.close()


def test_facebook_login(setup):
    driver.get("https://www.facebook.com/")


def test_amazon_login(setup):
    driver.get("https://www.amazon.in/")


def test_python_school(setup):
    driver.get("https://www.w3schools.com/python/default.asp")








