from PageObject.shop import ShopPage
from PageObject.home import HomePage


class TestShopPage(ShopPage, HomePage):
    def test_sort_price_by_price_asc(self):
        self.open_shop_page().click()
        self.sort_by("price")
        lis = []
        products_element = self.get_elements( ".woocommerce-Price-amount")
        for product in products_element:
            lis += [float(product.text[1:])]

        sorted_list = sorted(lis)
        assert lis[0] == sorted_list[0]

    def test_sort_price_by_price_desc(self):
        self.open_shop_page().click()
        self.sort_by("price-desc")
        lis = []
        products_element = self.get_elements( ".woocommerce-Price-amount")
        for product in products_element:
            lis += [float(product.text[1:])]
        sorted_list = sorted(lis, reverse=True)
        assert sorted_list[0] == 500.00

    def test_open_branded_converse_link(self):
        self.open_shop_page().click()
        self.click_on_branded_converse_link().click()
        assert "branded-converse" in self.driver.current_url

    def test_open_branded_converse_link_description(self):
        self.open_shop_page().click()
        self.click_on_branded_converse_link().click()
        assert "branded converse" in self.get_element(".woocommerce-product-details__short-description p").text

