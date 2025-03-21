import pytest

from python_pytest.base_class import BaseClass


@pytest.mark.usefixtures("load_data")
class TestExample2(BaseClass):

    def test_editProfile(self, load_data):
        log = self.get_logger()
        log.info(load_data[0])
        log.info(load_data[2])
        print(load_data[2])