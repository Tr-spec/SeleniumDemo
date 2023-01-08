import pytest


@pytest.fixture
def setup():
    print("get driver")
    print("driver.find_element by ID or XPATH")
    print("open facebook url")
    yield
    print("driver.maximize_window()")
    print("page title")
    print("driver.close()")


def test_amazon(setup):
    print("open amazon url")


def test_flipkart(setup):
    print("open flipkart url")



