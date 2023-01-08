import pytest


@pytest.mark.smoke
def test_1():
    a = 10
    b = 10
    result = a + b
    assert result == 10


@pytest.mark.regression
def test_2():
    a = 10
    b = 10
    assert a == b


@pytest.mark.smoke
def test_3():
    a = 10
    b = 10
    result = a + b
    assert result == 10


@pytest.mark.regression
def test_4():
    a = 10
    b = 10
    assert a == b


@pytest.mark.smoke
@pytest.mark.regression
def test_4():
    a = 10
    b = 10
    assert a == b


@pytest.mark.regression
@pytest.mark.smoke
def test_t4():
    x = 10
    y = 20
    result = x + y
    assert result == 30


@pytest.mark.swapnil
def test_check_in():
    name = "Credence"
    message = "Credence is the best place to learn and also extended family"
    assert name in message  ## in =>  like operator or contains function


@pytest.mark.regression
def test_check_is():
    name = "Credence"
    message = "Credence is the best place to learn and also extended family"
    assert name is message  # is =>  equal to


@pytest.mark.swapnil
def test_s():
    name = "swapnil"
    message = "swapnil shastrakar"
    assert name in message


@pytest.mark.swapnil
def test_w():
    name = "swapnil"
    message = "swapnil shastrakar"
    assert name is message


