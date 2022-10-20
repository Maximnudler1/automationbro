from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class ShopPage:
    def __init__(self, driver):
        self.driver = driver

    """page number 1"""

    sorting = (By.CSS_SELECTOR, '.orderby')

    search_input = (By.CSS_SELECTOR, 'woocommerce-product-search-field-0')
    search_button = (By.CSS_SELECTOR,'button[type=submit]')

    all_element_prices = (By.CSS_SELECTOR, '.woocommerce-Price-amount')

    branded_converse_link = (By.XPATH,'//h2[text()="Branded Converse"]')
    branded_converse_add_to_cart = (By.CSS_SELECTOR,'a[data-product_id="359"]')

    canon_link = (By.XPATH,'//h2[text()="Canon Antique Camera"]')
    canon_add_to_cart = (By.CSS_SELECTOR,'a[data-product_id="374"]')

    converse_link = (By.XPATH, '//h2[text()="Converse"]')
    converse_add_to_cart = (By.CSS_SELECTOR,'a[data-product_id="376"]')

    headphone_link = (By.XPATH,'//h2[text()="Headphone"]')
    headphone_add_to_cart = (By.CSS_SELECTOR,'a[data-product_id="361"]')

    ladies_jeans_link = (By.XPATH, '//h2[text()="Ladies Jeans"]')
    ladies_jeans_add_to_cart = (By.CSS_SELECTOR,'a[data-product_id="357"]')

    mini_speaker_link = (By.XPATH, '//h2[text()="Mini Speaker"]')
    mini_speaker_add_to_cart = (By.CSS_SELECTOR,'a[data-product_id="363"]')

    printed_skirt_link = (By.XPATH,'//h2[text()="Printed Skirt"]')
    printed_skirt_add_to_cart = (By.CSS_SELECTOR,'a[data-product_id="365"]')

    suit_link = (By.XPATH,'//h2[text()="Suits"]')
    suit_add_to_cart =(By.CSS_SELECTOR,'a[data-product_id="373"]')

    toys_link = (By.XPATH,'//h2[text()="Toys"]')
    toys_add_to_cart = (By.CSS_SELECTOR,'a[data-product_id="375"]')

    next_page_link = (By.CSS_SELECTOR,'.next')
    page_number_two = (By.XPATH,"(//a[contains(@href,'page/2/')])[1]")

    scroll_to_top = (By.CSS_SELECTOR, '.tg-icon-arrow-up')
    go_to_cart = (By.XPATH,'(//i[@class="tg-icon tg-icon-shopping-cart"])[1]')

    clothes_categories = (By.CSS_SELECTOR,'a[href*=clothes]')
    shoes_categories = (By.CSS_SELECTOR,'a[href*= shoes]')
    uncategorized_categories = (By.CSS_SELECTOR,'a[href*= uncategorized]')
    watch_categories = (By.CSS_SELECTOR,'li[class*=cat-item-18] a')

    """page number 2"""
    watch_link = (By.XPATH,'//h2[text()="Watch"]')
    watch_add_to_cart = (By.CSS_SELECTOR, 'a[data-product_id="377"]')

    zurich_watch = (By.XPATH, '//h2[text()="Zurich Watch"]')
    zurich_watch_add_to_cart = (By.XPATH, 'a[data-product_id="378"]')

    def sort_by(self, value):
        select = Select(self.driver.find_element(*ShopPage.sorting))
        return select.select_by_value(value)

    def add_to_cart_branded_converse(self):
        return self.driver.find_element(*ShopPage.branded_converse_add_to_cart)

    def element_prices(self):
        return self.driver.find_elements(*ShopPage.all_element_prices)







