from selenium import webdriver

#Chrome driver
from selenium.webdriver.chrome.service import Service

service_obj = Service(r"C:\Users\ilsan\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service = service_obj)
driver.get("http://google.com")
print(driver.title)
print(driver.current_url)
driver.close()