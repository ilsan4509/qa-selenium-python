from selenium.webdriver.common.by import By

from python_self_framework.page_objects.page_checkout import CheckOutPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    # driver.find_element(By.CSS_SELECTOR, "a[href*='shop']")
    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "[name='name']")
    email = (By.NAME, "email")
    check = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@value='Submit']")
    message_success = (By.CSS_SELECTOR, "[class*='alert-success']")


    def shop_items(self):
        self.driver.find_element(*HomePage.shop).click()
        checkout_page = CheckOutPage(self.driver)
        return checkout_page

    def get_name(self):
        return self.driver.find_element(*HomePage.name)

    def get_email(self):
        return self.driver.find_element(*HomePage.email)

    def get_checkbox(self):
        return self.driver.find_element(*HomePage.check)

    def get_gender(self):
        return self.driver.find_element(*HomePage.gender)

    def get_submit(self):
        return self.driver.find_element(*HomePage.submit)

    def get_message_success(self):
        return self.driver.find_element(*HomePage.message_success)