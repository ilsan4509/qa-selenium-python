from selenium.webdriver.common.by import By

from python_self_framework.page_objects.page_home import HomePage
from python_self_framework.utilities.base_class import BaseClass

class TestOne(BaseClass):
    def test_e2e(self):
        log = self.get_logger()

        # Logic for adding a product to the shopping cart
        home_page = HomePage(self.driver)
        checkout_page = HomePage.shop_items(self) #driver.find_element(By.CSS_SELECTOR, "a[href*='shop']")
        log.info("getting all the titles")
        cards = checkout_page.get_card_title() # driver.find_element(By.CSS_SELECTOR, ".card-title a")

        i = -1
        for card in cards:
            i = i+1
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                checkout_page.get_card_footer()[i].click() # driver.find_element(By.CSS_SELECTOR, ".card-footer button").click()

        checkout_page.get_cart().click() # driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
        confirm_page = checkout_page.check_out_items()
        log.info("Entering country name as ind")
        # Logic for choose a country on dropdown
        self.driver.find_element(By.ID, "country").send_keys("ind")
        self.verify_link_presence("India")
        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        success_text = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        log.info("Text received from application is " + success_text)

        assert "Success! test Thank you!" in success_text



