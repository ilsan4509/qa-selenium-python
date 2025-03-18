from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Chrome Options

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized") #full maximization
# chrome_options.add_argument("--window-size=1920x1080")
# chrome_options.add_argument("headless") # headless mode
chrome_options.add_argument("--disable-gpu") #Disable GPU acceleration
chrome_options.add_argument("--ignore-certificate-errors") # ignore certificate errors


service_obj = Service(r"C:\Users\ilsan\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service = service_obj, options=chrome_options)
driver.get("https://rahulshettyacademy.com/angularpractice/")
# driver.maximize_window() # instead of --start-maximized
print(driver.title)

# input("Press Enter to close the browser...")