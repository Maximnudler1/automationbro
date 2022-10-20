from PageObject.home import HomePage
from PageObject.shop import ShopPage


class TestHomePage(HomePage):

    def test_open_about_link(self):
        self.open_about_page().click()
        assert "about" in self.driver.current_url

    def test_open_shop_link(self):
        self.open_shop_page().click()
        assert "shop" in self.driver.current_url

    def test_open_blog_link(self):
        self.open_blog_page().click()
        assert "blog" in self.driver.current_url

    def test_open_contact_link(self):
        self.open_contact_page().click()
        assert "contact" in self.driver.current_url

    def test_open_my_account_link(self):
        self.open_my_account_page().click()
        assert "account" in self.driver.current_url

    def test_searching_a_product(self):
        assert self.search_product("camera").is_displayed()

    def test_open_driver_io_link(self):
        self.open_get_started_web_driver_io_link().click()
        assert "Webdriver" in self.driver.title

    def test_open_learn_appium_link(self):
        self.open_learn_appium_link().click()
        assert "Appium" in self.driver.title

    def test_open_play_write_link(self):
        self.open_learn_play_write_link().click()
        assert "Playwright" in self.driver.title

    def test_open_all_images(self):
        images = self.open_all_images()

        for image in images:
            image.click()
            self.close_all_images()

    def test_open_silver_link(self):
        self.open_silver_plan().click()
        assert "Silver" in self.driver.current_url

    def test_gold_silver_link(self):
        self.open_gold_plan().click()
        assert "Gold" in self.driver.current_url

    def test_platinum_link(self):
        self.open_platinum_plan().click()
        assert "Platinum" in self.driver.current_url

    def test_successful_marketing_ads_pic(self):
        self.open_successful_marketing_ads_pic().click()
        assert "Successful Marketing" in self.driver.title

    def test_successful_marketing_read_more_ads(self):
        self.open_successful_marketing_read_more().click()
        assert "Successful Marketing" in self.driver.title

    def test_successful_building_your_business_ads_pic(self):
        self.open_successful_building_your_business_pic().click()
        assert "Building Your Business" in self.driver.title

    def test_successful_building_your_business_read_more_ads(self):
        self.open_successful_building_your_business_read_more().click()
        assert "Building Your Business" in self.driver.title

    def test_invest_your_money_ads_pic(self):
        self.open_invest_your_money_pic().click()
        assert "Invest Your Money" in self.driver.title

    def test_invest_your_money_read_more_ads(self):
        self.open_invest_your_money_read_more().click()
        assert "Invest Your Money" in self.driver.title

    def test_big_seminar_ads_pic(self):
        self.open_big_seminar_pic().click()
        assert "Big Seminar" in self.driver.title

    def test_big_seminar_read_more_ads(self):
        self.open_big_seminar_read_more().click()
        assert "Big Seminar" in self.driver.title

    def test_contact_us_button(self):
        self.click_on_contact_us_button().click()
        """ contact window opens in a new window tab"""
        contact_window = self.driver.window_handles[1]
        self.driver.switch_to.window(contact_window)
        assert "contact" in self.driver.current_url