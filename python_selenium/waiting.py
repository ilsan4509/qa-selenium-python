import time

from selenium import webdriver

#Chrome driver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"C:\Users\ilsan\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service = service_obj)

# waits in automation testing
# Implicit Wait
driver.implicitly_wait(5) # 5 seconds is time out

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2) #Waiting for search results
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")#List[]
count = len(results)
# assert count == 3

assert count > 0
for result in results:
    result.find_element(By.XPATH,"div/button").click() #Add all search results to the cart

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

print(driver.find_element(By.CLASS_NAME, "promoInfo").text)
# input("Press Enter to close the browser...")