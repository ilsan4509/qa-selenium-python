# Any pytest file should start with test_
# pytest method names should start with test
# Any code should be wrapped in method only
# Method name should have sense
# -k stands for method names execution, -s logs in out put  -v stands for more info metadata
# you can run specific file with py.test <filename>
# you can mark (tag) tests @pytest.mark.smoke and then run with -m
# you can skip tests with @pytest.mark.skip
# @pytest.mark.xfail
# fixtures are used as setup and tear down methods for test cases - conftest file to
#generalize fixture and make it available to all rest cases
import pytest

@pytest.mark.smoke  #py.test -m smoke -v -s
@pytest.mark.skip # for ignore
def test_first_program():
    msg = "Hello" #operations
    assert msg == "Hi", "Test failed because strings not match"

# py.test -k creditcard -v -s
def test_second_creditcard():
    a = 4
    b = 6
    assert a+2 == 6, "Addition do not match"

# @pytest.fixture()
# def setup():
#     print("I will be executing first")
#
# def test_fisxture_demo(setup):
#     print("I will execute steps in fixture_demo method")
