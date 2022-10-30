
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from PageObject.home import HomePage
from PageObject.my_account import MyAccount


@pytest.fixture()
def setup(request):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://practice.automationbro.com/")
    driver.maximize_window()
    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield
    driver.close()


# @pytest.fixture()
# def my_account(driver):
#     my_account = MyAccount(driver)
#     return my_account





