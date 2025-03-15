from selenium import webdriver

#Chrome driver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

name = "Seonggon"
service_obj = Service(r"C:\Users\ilsan\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service = service_obj)

# Java and JavaScript alert handling
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert
alertText = alert.text
print(alertText)
assert name in alertText # Verifying if the alert contains a name value
alert.accept()
#alert.dismiss()
