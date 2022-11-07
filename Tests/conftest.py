
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import desired_capabilities
from webdriver_manager.chrome import ChromeDriverManager

from PageObject.home import HomePage
from PageObject.my_account import MyAccount

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from selenium import webdriver

browsers =  ['firefox','chrome']



@pytest.fixture()
def setup(request):
    # for browser_name in browsers:

        # if browser_name == "chrome":
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--window-size=1420,1080')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(
        chrome_options=chrome_options)




    driver.get("https://practice.automationbro.com/")
    # driver.maximize_window()
    # driver.set_window_position(0, 0) and driver.set_window_size(1920, 1080)
    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield
    driver.close()










