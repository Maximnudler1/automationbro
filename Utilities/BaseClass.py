import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures('setup')
class BaseClass:

    def get_elements(self, locator):
        return self.driver.find_elements(By.CSS_SELECTOR, locator)