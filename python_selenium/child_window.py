from selenium import webdriver

#Chrome driver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Handling child window/tab

service_obj = Service(r"C:\Users\ilsan\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service = service_obj)
driver.implicitly_wait(2)

driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT, "Click Here").click()

# Identifying all open windows
window_opened = driver.window_handles
# Switching to another window
driver.switch_to.window(window_opened[1])
print(driver.find_element(By.TAG_NAME, "h3").text)
driver.close()

driver.switch_to.window(window_opened[0])
print(driver.find_element(By.TAG_NAME, "h3").text)
assert "Opening a new window" == driver.find_element(By.TAG_NAME, "h3").text

# input("Press Enter to close the browser...")
