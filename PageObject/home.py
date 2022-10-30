from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

from Utilities.BaseClass import BaseClass


class HomePage(BaseClass):



    """navigation bar"""

    home_link = (By.XPATH, '(//a[text()="Home"])[1]')
    about_link = (By.XPATH, '(//a[text()="About"])[1]')
    shop_link = (By.XPATH, '(//a[text()="Shop"])[1]')
    blog_link = (By.XPATH, '(//a[text()="Blog"])[1]')
    contact_link = (By.XPATH, '(//a[text()="Contact"])[1]')
    my_account_link = (By.XPATH, '(//a[text()="My account"])[1]')
    search_icon = (By.XPATH, '(//i[@class="tg-icon tg-icon-search"])[1]')
    search_input = (By.CSS_SELECTOR, '.header-action-list input[type=search]')
    search_result = (By.XPATH,f'//span[contains(text(),"Search results for:")]')

    """Begin your test automation journey!"""

    get_started_web_driver_io_link = (By.XPATH, "//a[contains(text(),'started with WebdriverIO')]")
    learn_appium_link = (By.XPATH, "//a[contains(text(),'Learn Mobile Automation')]")
    learn_play_write = (By.XPATH, "//a[contains(text(),'Playwright')]")
    """Our Awesome Portfolio"""
    images = (By.CSS_SELECTOR, '.gallery-item img')
    close_image = (By.CSS_SELECTOR, '.eicon-close')
#   8 images in the gallery, use find_elements

    """Plan & Pricing"""

    silver_plan = (By.CSS_SELECTOR, 'div[data-id=cb29a40] a')
    gold_plan = (By.CSS_SELECTOR, 'div[data-id="04e82b8"] a')
    platinum_plan = (By.CSS_SELECTOR, 'div[data-id="6f66a3f"] a')

    """Latest Posts & Articles"""

    successful_marketing_ads = (By.XPATH, "(//a[contains(text(),'Successful Marketing')])[1]")
    successful_marketing_read_more =(By.CSS_SELECTOR, 'div[data-id="2e7ba82"] a')

    building_your_business = (By.XPATH, "(//a[contains(text(),'Let’s Building')])[1]")
    building_your_business_read_more = (By.CSS_SELECTOR, 'div[data-id="bdcbbee"] a')

    invest_your_money = (By.XPATH,"(//a[contains(text(),'Invest Your Money')])[1]")
    invest_your_money_read_more = (By.CSS_SELECTOR, 'div[data-id="cdb9c94"] a')

    big_seminar = (By.XPATH, "(//a[contains(text(),'Big Seminar')])[1]")
    big_seminar_read_more = (By.CSS_SELECTOR, 'div[data-id="22207be"] span')

    contact_us = (By.CSS_SELECTOR, '#contact-us')

    def open_about_page(self):
        return self.driver.find_element(*HomePage.about_link)

    def open_shop_page(self):
        return self.driver.find_element(*HomePage.shop_link)

    def open_blog_page(self):
        return self.driver.find_element(*HomePage.blog_link)

    def open_contact_page(self):
        return self.driver.find_element(*HomePage.contact_link)

    def open_my_account_page(self):
        return self.driver.find_element(*HomePage.my_account_link)

    def search_product(self, product):
        self.driver.find_element(*HomePage.search_icon).click()
        self.driver.find_element(*HomePage.search_input).send_keys(product)
        self.driver.find_element(*HomePage.search_input).send_keys(Keys.ENTER)
        return self.driver.find_element(*HomePage.search_result)

    def open_get_started_web_driver_io_link(self):
        return self.driver.find_element(*HomePage.get_started_web_driver_io_link)

    def open_learn_appium_link(self):
        return self.driver.find_element(*HomePage.learn_appium_link)

    def open_learn_play_write_link(self):
        return self.driver.find_element(*HomePage.learn_play_write)

    def open_all_images(self):
        return self.driver.find_elements(*HomePage.images)

    def close_all_images(self):
        self.driver.find_element(*HomePage.close_image).click()

    def open_silver_plan(self):
        return self.driver.find_element(*HomePage.silver_plan)

    def open_gold_plan(self):
        return self.driver.find_element(*HomePage.gold_plan)

    def open_platinum_plan(self):
        return self.driver.find_element(*HomePage.platinum_plan)

    def open_successful_marketing_ads_pic(self):
        return self.driver.find_element(*HomePage.successful_marketing_ads)

    def open_successful_marketing_read_more(self):
        return self.driver.find_element(*HomePage.successful_marketing_ads)

    def open_successful_building_your_business_pic(self):
        return self.driver.find_element(*HomePage.building_your_business)

    def open_successful_building_your_business_read_more(self):
        return self.driver.find_element(*HomePage.building_your_business_read_more)

    def open_invest_your_money_pic(self):
        return self.driver.find_element(*HomePage.invest_your_money)

    def open_invest_your_money_read_more(self):
        return self.driver.find_element(*HomePage.invest_your_money_read_more)

    def open_big_seminar_pic(self):
        return self.driver.find_element(*HomePage.big_seminar)

    def open_big_seminar_read_more(self):
        return self.driver.find_element(*HomePage.big_seminar_read_more)

    def click_on_contact_us_button(self):
        return self.driver.find_element(*HomePage.contact_us)

















