import pytest


@pytest.mark.usefixtures("load_data")
class TestExample2:

    def test_editProfile(self, load_data):
        print(load_data[0])
        print(load_data[1])
        print(load_data[2])