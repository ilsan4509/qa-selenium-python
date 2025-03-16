from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Javascript - scroll, screenshot, headless mode

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless") # headless mode
chrome_options.add_argument("--ignore-certificate-errors") # ignore certificate errors

service_obj = Service(r"C:\Users\ilsan\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service = service_obj, options=chrome_options)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.execute_script("window.scrollBy(0,document.body.scrollHeight);") # scroll
driver.get_screenshot_as_file("screen.png") # screenshot
