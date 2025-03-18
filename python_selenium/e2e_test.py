from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service(r"C:\Users\ilsan\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service = service_obj)
driver.implicitly_wait(4)
driver.get("https://rahulshettyacademy.com/angularpractice/shop")


# Logic for adding a product to the shopping cart
driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

for product in products :
    product_name = product.find_element(By.XPATH, "div/h4/a").text
    if product_name == "Blackberry" :
        product.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
# Chrome console check $, $x("//button[@class='btn btn-success']")
driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()

# Logic for choose a country on dropdown
driver.find_element(By.ID, "country").send_keys("ind")
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, "India").click()
driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
success_text = driver.find_element(By.CLASS_NAME, "alert-success").text
assert "Success! Thank you!" in success_text
driver.close()

# input("Press Enter to close the browser...")