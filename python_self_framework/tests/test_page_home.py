import pytest

from python_self_framework.page_objects.page_home import HomePage
from python_self_framework.test_data.data_home import HomeData
from python_self_framework.utilities.base_class import BaseClass


class TestHomePage(BaseClass):

    def test_form_submission(self, get_deta):
        log = self.get_logger()
        home_page = HomePage(self.driver)
        log.info("first name is " + get_deta["firstName"])
        home_page.get_name().send_keys(get_deta["firstName"]) # home_page.get_name().send_keys(get_deta[0])
        home_page.get_email().send_keys(get_deta["email"]) # home_page.get_email().send_keys(get_deta[1])
        home_page.get_checkbox().click()
        self.select_option_by_text(home_page.get_gender(), get_deta["gender"]) # self.select_option_by_text(home_page.get_gender(), get_deta[2])

        home_page.get_submit().click()

        alert_text = home_page.get_message_success().text
        assert ("Success" in alert_text)

        self.driver.refresh()

    @pytest.fixture(params = HomeData.get_test_data("Testcase2"))
    def get_deta(self, request):
        return request.param
