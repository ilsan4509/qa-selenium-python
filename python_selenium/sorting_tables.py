from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Sorting Tables

browser_sorted_veggies_list = []
service_obj = Service(r"C:\Users\ilsan\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service = service_obj)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

# click on column header
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
# collect all veggie names -> veggieList(BrowserSorted)
veggie_web_elements = driver.find_elements(By.XPATH, "//tr/td[1]")
for ele in veggie_web_elements :
    browser_sorted_veggies_list.append(ele.text)

original_browser_sorted_veggies_list = browser_sorted_veggies_list.copy()

# Sort this veggieList(BrowserSorted) => newSortedList
browser_sorted_veggies_list.sort()
assert browser_sorted_veggies_list == original_browser_sorted_veggies_list

# input("Press Enter to close the browser...")