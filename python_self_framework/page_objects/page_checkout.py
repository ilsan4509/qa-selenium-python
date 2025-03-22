from selenium.webdriver.common.by import By


class CheckOutPage:
    def __init__(self, driver):
        self.driver = driver

    # driver.find_element(By.CSS_SELECTOR, ".card-title a")
    # driver.find_element(By.CSS_SELECTOR, ".card-footer button")
    # driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']")
    # driver.find_element(By.XPATH, "//button[@class='btn btn-success']")
    card_title = (By.CSS_SELECTOR, ".card-title a")
    card_footer = (By.CSS_SELECTOR, ".card-footer button")
    cart = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    check_out = (By.XPATH, "//button[@class='btn btn-success']")

    def get_card_title(self):
        return self.driver.find_elements(*CheckOutPage.card_title)

    def get_card_footer(self):
        return self.driver.find_elements(*CheckOutPage.card_footer)

    def get_cart(self):
        return self.driver.find_element(*CheckOutPage.cart)

    def check_out_items(self):
        return self.driver.find_element(*CheckOutPage.check_out)