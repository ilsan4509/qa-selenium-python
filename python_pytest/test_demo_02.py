# Any pytest file should start with test_
# pytest method names should start with test
# Any code should be wrapped in method only

def test_first_program():
    msg = "Hello"
    assert msg == "Hi", "Test failed because strings not match"


def test_second_program():
    a = 4
    b = 6
    assert a+2 == 6, "Addition do not match"