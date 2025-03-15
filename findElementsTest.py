import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# -- Chrome
service_obj = Service(r"C:\Users\ilsan\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service = service_obj)

# Testing E-commerce
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element(By.ID,"autosuggest").send_keys("ind")
#time.sleep(2) # Wait for the search suggestion dropdown (dynamic text)

countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
print(len(countries))

for country in countries:
    if country.text == "India":
        country.click()
        break

# Validate dynamic text
# print(driver.find_element(By.ID, "autosuggest").text)
assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"
# assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "Hong Kong"
