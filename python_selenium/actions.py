from selenium import webdriver
from selenium.webdriver import ActionChains

#Chrome driver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# ActionChains

service_obj = Service(r"C:\Users\ilsan\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service = service_obj)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
action = ActionChains(driver)

# action.click_and_hold() # (Frequently used on mobile)
# action.double_click()
# action.context_click() # Right-click
# action.drag_and_drop()
# action.move_to_element() # Move the mouse to the specified location

# The ActionChains object stores multiple actions in a chain format, and they are executed only when perform() is called.
# In other words, methods like .move_to_element(), .context_click(), and .click() only prepare the actions,
# but perform() must be called to actually execute them in the browser.
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()

# input("Press Enter to close the browser...")