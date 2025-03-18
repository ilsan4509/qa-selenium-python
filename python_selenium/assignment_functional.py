import time
from selenium import webdriver

#Chrome driver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# Validate search results, Check price conditions after promotion

expectedList = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg'] # Expected values in search results
actualList = [] # Test search results

service_obj = Service(r"C:\Users\ilsan\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service = service_obj)

# Create WebDriverWait instance
wait = WebDriverWait(driver, 10)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2) #Waiting for search results


results = driver.find_elements(By.XPATH, "//div[@class='products']/div")#List[]
count = len(results)
assert count > 0
for result in results:
    actualList.append(result.find_element(By.XPATH, "h4").text) #Add all name of products
    result.find_element(By.XPATH, "div/button").click() #Add all search results to the cart

assert expectedList == actualList

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

#Sum validation
wait.until(expected_conditions.presence_of_all_elements_located((By.CSS_SELECTOR, "tr td:nth-child(5) p")))
prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
sum_price = 0

for price in prices:
    sum_price = sum_price + int(price.text)
print(sum_price)
totalAmount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)

assert sum_price == totalAmount # Validate search results

# Wait until .promoCode is loaded
wait.until(expected_conditions.presence_of_all_elements_located((By.CSS_SELECTOR, ".promoCode")))
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

# Wait until .promoInfo is loaded
wait.until(expected_conditions.presence_of_all_elements_located((By.CSS_SELECTOR, ".promoInfo")))
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)

# Check price conditions after promotion
discountedAmount = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)

print(discountedAmount)
assert  totalAmount > discountedAmount

# input("Press Enter to close the browser...")