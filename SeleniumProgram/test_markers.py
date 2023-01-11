import sys

import pytest


@pytest.mark.skip  # @pytest.mark.skip
def test_1():
    a = 10
    b = 20

    assert a == b


@pytest.mark.skip
def test_2():
    a = 10
    b = 10
    result = a + b
    assert result == 20


# if skipif Failed = UnSkipped
@pytest.mark.skipif(sys.version_info <= (3, 7, 10), reason=f" {sys.version_info}version not supported")
def test_3():
    x = 20
    y = 20

    assert x == y


# if skipif True = Skipped
@pytest.mark.skipif(sys.version_info >= (3, 7), reason=f"{sys.version_info} value not supported")
def test_4():
    a = "credence"
    assert a.__contains__("h")


@pytest.mark.xfail
def test_5():  # @pytest.mark.xfail
    a = 100
    b = 100

    assert a == b  # xpassed


@pytest.mark.xfail
def test_6():
    a = 10
    b = 20

    assert a > b  # xfailed


@pytest.mark.xfail
def test_006():
    a = 1000
    b = 20000
    result = a + b

    assert result == 200


@pytest.mark.xfail
def test_007():
    a = 100
    b = 200
    result = a + b

    assert result == 300
