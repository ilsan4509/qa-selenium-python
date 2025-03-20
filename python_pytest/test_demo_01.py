# Any pytest file should start with test_
# pytest method names should start with test
# Any code should be wrapped in method only

# CMD - pip install pytest, py.test -v -s, py.test test_example.py -v -s
import pytest

@pytest.mark.smoke
def test_first_program(setup):
    print("Hello")



# py.test -k creditcard -v -s
@pytest.mark.xfailv  # when need not report
def test_second_geet_creditcard():
    print("Meow")


def test_cross_browser(cross_browser):
    print(cross_browser[1])

