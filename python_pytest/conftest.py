import pytest

# conftest - important file name
@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield
    print("I will executed last")

@pytest.fixture()
def load_data():
    print("user profile data is being created")
    return ["Seonggon", "Jayden", "google.com"]


@pytest.fixture(params=[("Chrome", "Seonggon", "name"), ("Firefox", "tada"), ("Edge", "Micro")])
def cross_browser(request):
    return request.param

