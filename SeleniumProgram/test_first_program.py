def test_first():
    a = 10
    b = 20

    assert a == b


def test_second():
    a = 10
    b = 20

    assert a != b


def test_third():
    a = 10
    b = 20

    assert b == a


def test_four():
    a = 10
    b = 20

    assert a < b


def test_five():
    a = "swapnil"
    assert a.__contains__("s")


def test_six():
    a = 10
    b = 20
    result = a + b
    assert result == 30







