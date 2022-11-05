
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import desired_capabilities
from webdriver_manager.chrome import ChromeDriverManager

from PageObject.home import HomePage
from PageObject.my_account import MyAccount

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from selenium import webdriver
from seleniumbase import BaseCase as driver


browsers =  ['firefox','chrome']



@pytest.fixture()
def setup(request):
    for browser_name in browsers:

        # if browser_name == "chrome":
    #
    # chrome_options = webdriver.ChromeOptions()
    # driver = webdriver.Remote(
    #     command_executor="http://localhost:4444/wd/hub",
    #     options=chrome_options
    # )
    #     elif browser_name == "firefox":
    #
    #         firefox_options = webdriver.FirefoxOptions()
    #         driver = webdriver.Remote(
    #             command_executor='http://localhost:4444/wd/hub',
    #             options=firefox_options
    #
    #         )
    # driver = webdriver.Remote(command_executor="http://localhost:4444/wd/hub",
    #                           desired_capabilities=desired_capabilities.DesiredCapabilities.FIREFOX)
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver = webdriver.Chrome()
    driver.get("https://practice.automationbro.com/")
    # driver.maximize_window()
    # driver.set_window_position(0, 0) and driver.set_window_size(1920, 1080)
    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield
    driver.close()










