import pytest


@pytest.mark.parametrize("username, password",
                         [
                             ('user1', 'pass1'),
                             ('user2', 'pass2'),
                             ('user3', 'pass3'),
                             ('user4', 'pass4'),
                             ('user5', 'pass5')
                         ]
                         )
def test_login(username, password):
    print(f"User Name = {username} Password = {password}")
    if username == 'user4' and password == 'pass4':
        assert True
    else:
        assert False
