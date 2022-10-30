import time

from PageObject.my_account import MyAccount
from PageObject.home import HomePage


class TestMyAccountPage(MyAccount,HomePage):

    def test_register_to_the_website(self):

        self.open_my_account_page().click()
        self.insert_user_name_on_register_part('maximnudler22')
        self.insert_email_on_register_part("maximtes3t12@gmail.com")
        self.insert_password_on_register_part('maxim132345678!')
        self.register_btn().click()
        assert "maximnudler22" in self.hello_user_name()

    def test_register_without_insert_username_error_handling(self):
        self.open_my_account_page().click()
        self.insert_email_on_register_part("maximtest12@gmail.com")
        self.insert_password_on_register_part('maxim12345678!')
        self.register_btn().click()
        assert "Please enter a valid account username." in self.error_message()

    def test_register_without_insert_email_error_handling(self):
        self.open_my_account_page().click()
        self.insert_user_name_on_register_part('maximnudler2')
        self.insert_password_on_register_part('maxim12345678!')
        self.register_btn().click()
        assert "Please provide a valid email address." in self.error_message()

    def test_register_without_insert_password_error_handling(self):
        self.open_my_account_page().click()
        self.insert_email_on_register_part("maximtest12@gmail.com")
        self.insert_user_name_on_register_part('maximnudler2')
        self.register_btn().click()
        assert "Please enter an account password." in self.error_message()

    def test_log_in_with_exists_user(self):
        self.open_my_account_page().click()
        self.insert_log_in_username("maximtest1234")
        self.insert_log_in_password("maximnudler")
        self.remember_me_btn().click()
        self.log_in_btn().click()
        assert "maximtest1234" in self.hello_user_name()

