import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# For this to work we need to add a command line option and provide the cmdopt through a fixture function
# CMD: py.test --browser_name firefox
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope = "class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        service_obj = Service(r"C:\Users\ilsan\chromedriver-win64\chromedriver.exe")
        driver = webdriver.Chrome(service = service_obj)
    elif browser_name == "firefox":
        service_obj = Service(r"C:\Users\ilsan\geckodriver-v0.35.0-win64\geckodriver.exe")
        driver = webdriver.Firefox(service = service_obj)
    elif browser_name == "Edge":
        service_obj = Service(r"C:\Users\ilsan\edgedriver_win64\msedgedriver.exe")
        driver = webdriver.Edge(service = service_obj)

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

