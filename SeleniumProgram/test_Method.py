import pytest


class TestClass:

    @pytest.fixture
    def setup(self):
        print("Setup Method Opening")
        yield
        print("Setup Method Closing")

    def test_1(self, setup):
        print("This is method 1")

    def test_2(self, setup):
        print("This is method 2")
