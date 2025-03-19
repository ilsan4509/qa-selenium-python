import pytest

# conftest - important file name
@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield
    print("I will executed last")