import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver = None

# For this to work we need to add a command line option and provide the cmdopt through a fixture function
# CMD: py.test --browser_name firefox
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope = "class")
def setup(request):
    global driver
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

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
    """
    # Get the pytest-html plugin instance to modify the test report
    pytest_html = item.config.pluginmanager.getplugin('html')
    # Yield the test outcome (setup, call, or teardown)
    outcome = yield
    report = outcome.get_result() # Get the result of the test execution
    extra = getattr(report, 'extra', []) # Get extra report data

    # Capture screenshot only during 'setup' or 'call' phase (not during teardown) / 'setup' 또는 'call' 단계에서만 스크린샷을 캡처함 ('teardown' 단계는 제외)
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # If test failed, take a screenshot and embed it in the report
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                # Generate an HTML snippet to embed the screenshot in the report
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html)) # Add the HTML snippet to the report
        report.extra = extra


def _capture_screenshot(name):
    """
        Captures a screenshot and saves it as a file.
        name: The name of the file where the screenshot will be saved
    """
    driver.get_screenshot_as_file(name)