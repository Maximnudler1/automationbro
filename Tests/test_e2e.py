from PageObject.my_account import MyAccount
from Tests.conftest import my_account
from Utilities.BaseClass import BaseClass
from PageObject.home import HomePage
from PageObject.shop import ShopPage


class TestAutomationBro(HomePage):
    pass



    # def test_register_to_the_website(self):
    #     home_p = HomePage(self.driver)
    #     home_p.open_my_account_page().click()
    #     account_p = MyAccount(self.driver)
    #     account_p.insert_user_name_on_register_part('maximnudler2')
    #     account_p.insert_email_on_register_part("maximtest12@gmail.com")
    #     account_p.insert_password_on_register_part('maxim12345678!')
    #     account_p.register_btn().click()
    #     assert "maximnudler2" in account_p.hello_user_name()
    #
    # def test_register_without_insert_username_error_handling(self):
    #     home_p = HomePage(self.driver)
    #     home_p.open_my_account_page().click()
    #     account_p = MyAccount(self.driver)
    #     account_p.insert_email_on_register_part("maximtest12@gmail.com")
    #     account_p.insert_password_on_register_part('maxim12345678!')
    #     account_p.register_btn().click()
    #     assert "Please enter a valid account username." in account_p.error_message()
    #
    # def test_register_without_insert_email_error_handling(self):
    #     home_p = HomePage(self.driver)
    #     home_p.open_my_account_page().click()
    #     account_p = MyAccount(self.driver)
    #     account_p.insert_user_name_on_register_part('maximnudler2')
    #     account_p.insert_password_on_register_part('maxim12345678!')
    #     account_p.register_btn().click()
    #     assert "Please provide a valid email address." in account_p.error_message()
    #
    # def test_register_without_insert_password_error_handling(self):
    #     home_p = HomePage(self.driver)
    #     home_p.open_my_account_page().click()
    #     account_p = MyAccount(self.driver)
    #     account_p.insert_email_on_register_part("maximtest12@gmail.com")
    #     account_p.insert_user_name_on_register_part('maximnudler2')
    #     account_p.register_btn().click()
    #     assert "Please enter an account password." in account_p.error_message()
    #
    # def test_log_in_with_exists_user(self):
    #     home_p = HomePage(self.driver)
    #     home_p.open_my_account_page().click()
    #     account_p = MyAccount(self.driver)
    #     account_p.insert_log_in_username("maximtest1234")
    #     account_p.insert_log_in_password("maximnudler")
    #     account_p.remember_me_btn().click()
    #     account_p.log_in_btn().click()
    #     assert "maximtest1234" in account_p.hello_user_name()
    #
    # def test_sort_price_by_price_asc(self):
    #     home_p = HomePage(self.driver)
    #     home_p.open_shop_page().click()
    #     shop_p = ShopPage(self.driver)
    #     shop_p.sort_by("price")
    #     lis = []
    #     products_element = TestAutomationBro.get_elements(self, ".woocommerce-Price-amount")
    #     for product in products_element:
    #         lis += [float(product.text[1:])]
    #
    #     sorted_list = sorted(lis)
    #     assert lis[0] == sorted_list[0]
    #
    # def test_sort_price_by_price_desc(self):
    #     home_p = HomePage(self.driver)
    #     home_p.open_shop_page().click()
    #     shop_p = ShopPage(self.driver)
    #     shop_p.sort_by("price-desc")
    #     lis = []
    #     products_element = TestAutomationBro.get_elements(self, ".woocommerce-Price-amount")
    #     for product in products_element:
    #         lis += [float(product.text[1:])]
    #
    #     sorted_list = sorted(lis, reverse=True)
    #     assert sorted_list[0] == 500.00
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #








































