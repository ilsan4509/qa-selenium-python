from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from python_self_framework.page_objects.page_home import HomePage
from python_self_framework.utilities.base_class import BaseClass

class TestOne(BaseClass):
    def test_e2e(self):
        # Logic for adding a product to the shopping cart

        home_page = HomePage(self.driver)
        checkout_page = HomePage.shop_items(self) #driver.find_element(By.CSS_SELECTOR, "a[href*='shop']")
        cards = checkout_page.get_card_title() # driver.find_element(By.CSS_SELECTOR, ".card-title a")

        i = -1
        for card in cards:
            i = i+1
            cardText = card.text
            if cardText == "Blackberry":
                checkout_page.get_card_footer()[i].click() # driver.find_element(By.CSS_SELECTOR, ".card-footer button").click()

        checkout_page.get_cart().click() # driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
        confirm_page = checkout_page.check_out_items()

        # Logic for choose a country on dropdown
        self.driver.find_element(By.ID, "country").send_keys("ind")
        self.verify_link_presence("India")
        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        success_text = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        assert "Success! Thank you!" in success_text



