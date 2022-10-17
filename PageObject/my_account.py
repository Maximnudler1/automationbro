from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class MyAccount:

    def __init__(self, driver):
        self.driver = driver

    """Register"""
    user_name = (By.CSS_SELECTOR, '#reg_username')
    email_address = (By.CSS_SELECTOR, '#reg_email')
    password = (By.CSS_SELECTOR, "#reg_password")
    show_password = (By.XPATH,' //form[contains(@class,"register")]/p[3]/span/span')
    register_button = (By.CSS_SELECTOR, 'button[name=register]')
    hello_user = (By.XPATH, '//strong[1]')
    error_message_register = (By.CSS_SELECTOR, '.woocommerce-error li')

    """Log in"""
    log_in_user_name = (By.CSS_SELECTOR, '#username')
    log_in_password = (By.CSS_SELECTOR, '#password')
    log_in_remember = (By.CSS_SELECTOR, '#rememberme')
    log_in_button = (By.CSS_SELECTOR, 'button[name="login"]')

    """Register"""
    def insert_user_name_on_register_part(self, username):
        return self.driver.find_element(*MyAccount.user_name).send_keys(username)

    def insert_email_on_register_part(self, email):
        return self.driver.find_element(*MyAccount.email_address).send_keys(email)

    def insert_password_on_register_part(self, password):
        return self.driver.find_element(*MyAccount.password).send_keys(password)

    def show_password_btn(self):
        return self.driver.find_element(*MyAccount.show_password)

    def register_btn(self):
        return self.driver.find_element(*MyAccount.register_button)

    def hello_user_name(self):
        return self.driver.find_element(*MyAccount.hello_user).text

    def error_message(self):
        return self.driver.find_element(*MyAccount.error_message_register).text

    """Log in"""
    def insert_log_in_username(self, username):
        return self.driver.find_element(*MyAccount.log_in_user_name).send_keys(username)

    def insert_log_in_password(self, password):
        return self.driver.find_element(*MyAccount.log_in_password).send_keys(password)

    def remember_me_btn(self):
        return self.driver.find_element(*MyAccount.log_in_remember)

    def log_in_btn(self):
        return self.driver.find_element(*MyAccount.log_in_button)
















