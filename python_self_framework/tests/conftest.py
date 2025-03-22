import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope = "class")
def setup(request):
    service_obj = Service(r"C:\Users\ilsan\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

