import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select

@pytest.mark.usefixtures("setup")
class BaseClass:

    def verify_link_presence(self, text):
        """
        Waits until a link with the given text is present on the page.
        :param text: The visible text of the link to wait for (기다릴 링크의 표시 텍스트)
        """
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))


    def select_option_by_text(self, locator, text):
        """
        Selects an option in a dropdown menu based on the visible text.
        :param locator: The dropdown WebElement
        :param text: The visible text of the option to be selected
        """
        sel = Select(locator)
        sel.select_by_visible_text(text)

    def get_logger(self):
        """
        Creates and configures a logger for test execution.

        The logger writes logs to a file (logfile.log) with a timestamp, log level,
        function name, and message.

        :return: Configured logger instance
        """
        logger_name = inspect.stack()[1][3] # Get the function name dynamically
        logger = logging.getLogger(logger_name)
        # Create a file handler that writes log messages to "logfile.log"
        fileHandler = logging.FileHandler("logfile.log")
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter) # Apply formatter to file handler

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger # Return configured logger instance