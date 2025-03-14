from pyexpat.errors import messages
from selenium import webdriver

#Chrome driver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# -- Chrome
service_obj = Service(r"C:\Users\ilsan\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service = service_obj)

driver.get("https://rahulshettyacademy.com/angularpractice/")

# ID, Xpath, CSSSelector, Classname, name, linkText
driver.find_element(By.NAME, "email").send_keys("jjjayden@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click()
# Chrome Plugin - ChroPath
# Xpath - //tagname[@attribute='value'] -> //input[@type='submit']
# CSS - //tagname[@attribute='value'] -> //input[@type='submit'], #id,  .classname
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("12423231242")
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()
driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert "Success" in message

# using index for targeting
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("wfwfax")
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").clear()