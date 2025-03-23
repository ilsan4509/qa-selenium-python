from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from python_selenium.alerts import alert
from python_self_framework.page_objects.page_home import HomePage
from python_self_framework.utilities.base_class import BaseClass


class TestHomePage(BaseClass):

    def test_form_submission(self):
        home_page = HomePage(self.driver)
        home_page.get_name().send_keys("Jayden")
        home_page.get_email().send_keys("Jayden@mail.com")
        home_page.get_checkbox().click()
        self.select_option_by_text(home_page.get_gender(), "Male")

        home_page.get_submit().click()

        alert_text = home_page.get_message_success().text

        assert ("Success" in alert_text)