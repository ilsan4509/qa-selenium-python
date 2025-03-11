from selenium import webdriver

#Chrome driver
from selenium.webdriver.chrome.service import Service

# -- Chrome
service_obj = Service(r"C:\Users\ilsan\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service = service_obj)

# -- Firefox
# service_obj = Service(r"C:\Users\ilsan\geckodriver-v0.35.0-win64\geckodriver.exe")
# driver = webdriver.Firefox(service = service_obj)

# -- MicroEdge
# service_obj = Service(r"C:\Users\ilsan\edgedriver_win64\msedgedriver.exe")
# driver = webdriver.Edge(service = service_obj)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/")
print(driver.title)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
# driver.minimize_window()
driver.back()
driver.refresh()
driver.forward()
driver.close()