from Utilities.BaseClass import BaseClass
from PageObject.home import HomePage
from PageObject.shop import ShopPage


class TestAutomationBro(BaseClass):


    def test_open_about_link(self):
        home_p = HomePage(self.driver)
        home_p.open_about_page().click()
        assert "about" in self.driver.current_url

    def test_open_shop_link(self):
        home_p = HomePage(self.driver)
        home_p.open_shop_page().click()
        assert "shop" in self.driver.current_url

    def test_open_blog_link(self):
        home_p = HomePage(self.driver)
        home_p.open_blog_page().click()
        assert "blog" in self.driver.current_url

    def test_open_contact_link(self):
        home_p = HomePage(self.driver)
        home_p.open_contact_page().click()
        assert "contact" in self.driver.current_url

    def test_open_my_account_link(self):
        home_p = HomePage(self.driver)
        home_p.open_my_account_page().click()
        assert "account" in self.driver.current_url

    def test_searching_a_product(self):
        home_p = HomePage(self.driver)
        assert home_p.search_product("camera").is_displayed()

    def test_open_driver_io_link(self):
        home_p = HomePage(self.driver)
        home_p.open_get_started_web_driver_io_link().click()
        assert "Webdriver" in self.driver.title

    def test_open_learn_appium_link(self):
        home_p = HomePage(self.driver)
        home_p.open_learn_appium_link().click()
        assert "Appium" in self.driver.title

    def test_open_play_write_link(self):
        home_p = HomePage(self.driver)
        home_p.open_learn_play_write_link().click()
        assert "Playwright" in self.driver.title

    def test_open_all_images(self):
        home_p = HomePage(self.driver)
        images = home_p.open_all_images()

        for image in images:
            image.click()
            home_p.close_all_images()

    def test_open_silver_link(self):
        home_p = HomePage(self.driver)
        home_p.open_silver_plan().click()
        assert "Silver" in self.driver.current_url

    def test_gold_silver_link(self):
        home_p = HomePage(self.driver)
        home_p.open_gold_plan().click()
        assert "Gold" in self.driver.current_url

    def test_platinum_link(self):
        home_p = HomePage(self.driver)
        home_p.open_platinum_plan().click()
        assert "Platinum" in self.driver.current_url

    def test_successful_marketing_ads_pic(self):
        home_p = HomePage(self.driver)
        home_p.open_successful_marketing_ads_pic().click()
        assert "Successful Marketing" in self.driver.title

    def test_successful_marketing_read_more_ads(self):
        home_p = HomePage(self.driver)
        home_p.open_successful_marketing_read_more().click()
        assert "Successful Marketing" in self.driver.title

    def test_successful_building_your_business_ads_pic(self):
        home_p = HomePage(self.driver)
        home_p.open_successful_building_your_business_pic().click()
        assert "Building Your Business" in self.driver.title

    def test_successful_building_your_business_read_more_ads(self):
        home_p = HomePage(self.driver)
        home_p.open_successful_building_your_business_read_more().click()
        assert "Building Your Business" in self.driver.title

    def test_invest_your_money_ads_pic(self):
        home_p = HomePage(self.driver)
        home_p.open_invest_your_money_pic().click()
        assert "Invest Your Money" in self.driver.title

    def test_invest_your_money_read_more_ads(self):
        home_p = HomePage(self.driver)
        home_p.open_invest_your_money_read_more().click()
        assert "Invest Your Money" in self.driver.title

    def test_big_seminar_ads_pic(self):
        home_p = HomePage(self.driver)
        home_p.open_big_seminar_pic().click()
        assert "Big Seminar" in self.driver.title

    def test_big_seminar_read_more_ads(self):
        home_p = HomePage(self.driver)
        home_p.open_big_seminar_read_more().click()
        assert "Big Seminar" in self.driver.title

    def test_contact_us_button(self):
        home_p = HomePage(self.driver)
        home_p.click_on_contact_us_button().click()
        """ contact window opens in a new window tab"""
        contact_window = self.driver.window_handles[1]
        self.driver.switch_to.window(contact_window)
        assert "contact" in self.driver.current_url

    def test_register_to_the_website(self):
        home_p = HomePage(self.driver)
        home_p.open_my_account_page().click()
        account_p = MyAccount(self.driver)
        account_p.insert_user_name_on_register_part('maximnudler2')
        account_p.insert_email_on_register_part("maximtest12@gmail.com")
        account_p.insert_password_on_register_part('maxim12345678!')
        account_p.register_btn().click()
        assert "maximnudler2" in account_p.hello_user_name()

    def test_register_without_insert_username_error_handling(self):
        home_p = HomePage(self.driver)
        home_p.open_my_account_page().click()
        account_p = MyAccount(self.driver)
        account_p.insert_email_on_register_part("maximtest12@gmail.com")
        account_p.insert_password_on_register_part('maxim12345678!')
        account_p.register_btn().click()
        assert "Please enter a valid account username." in account_p.error_message()

    def test_register_without_insert_email_error_handling(self):
        home_p = HomePage(self.driver)
        home_p.open_my_account_page().click()
        account_p = MyAccount(self.driver)
        account_p.insert_user_name_on_register_part('maximnudler2')
        account_p.insert_password_on_register_part('maxim12345678!')
        account_p.register_btn().click()
        assert "Please provide a valid email address." in account_p.error_message()

    def test_register_without_insert_password_error_handling(self):
        home_p = HomePage(self.driver)
        home_p.open_my_account_page().click()
        account_p = MyAccount(self.driver)
        account_p.insert_email_on_register_part("maximtest12@gmail.com")
        account_p.insert_user_name_on_register_part('maximnudler2')
        account_p.register_btn().click()
        assert "Please enter an account password." in account_p.error_message()

    def test_log_in_with_exists_user(self):
        home_p = HomePage(self.driver)
        home_p.open_my_account_page().click()
        account_p = MyAccount(self.driver)
        account_p.insert_log_in_username("maximtest1234")
        account_p.insert_log_in_password("maximnudler")
        account_p.remember_me_btn().click()
        account_p.log_in_btn().click()
        assert "maximtest1234" in account_p.hello_user_name()

    def test_sort_price_by_price_asc(self):
        home_p = HomePage(self.driver)
        home_p.open_shop_page().click()
        shop_p = ShopPage(self.driver)
        shop_p.sort_by("price")
        lis = []
        products_element = TestAutomationBro.get_elements(self, ".woocommerce-Price-amount")
        for product in products_element:
            lis += [float(product.text[1:])]

        sorted_list = sorted(lis)
        assert lis[0] == sorted_list[0]

    def test_sort_price_by_price_desc(self):
        home_p = HomePage(self.driver)
        home_p.open_shop_page().click()
        shop_p = ShopPage(self.driver)
        shop_p.sort_by("price-desc")
        lis = []
        products_element = TestAutomationBro.get_elements(self, ".woocommerce-Price-amount")
        for product in products_element:
            lis += [float(product.text[1:])]

        sorted_list = sorted(lis, reverse=True)
        assert sorted_list[0] == 500.00

























































