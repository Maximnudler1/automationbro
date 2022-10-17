from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class CartCheckout:
    def __init__(self,driver):
        self.driver = driver

    """cart page"""

    select_file = (By.CSS_SELECTOR, '#upfile_1')
    upload_file = (By.CSS_SELECTOR, '#upload_1')

    update_cart = (By.CSS_SELECTOR, 'button[name="update_cart"]')
    coupon_input = (By.CSS_SELECTOR, 'input[id=coupon_code]')
    apply_coupon = (By.CSS_SELECTOR, 'button[name="apply_coupon"]')
    proceed_to_checkout = (By.CSS_SELECTOR, '.wc-proceed-to-checkout a')

    """check out page"""
    returning_customers = (By.CSS_SELECTOR, '.showlogin')
    have_coupon = (By.CSS_SELECTOR, '.showcoupon')

    """billing address"""
    first_name = (By.CSS_SELECTOR, '#billing_first_name')
    last_name = (By.CSS_SELECTOR, '##billing_last_name')
    company_name = (By.CSS_SELECTOR, '#billing_company')
    region = (By.CSS_SELECTOR, '#billing_country')
    house = (By.CSS_SELECTOR, 'input[id=billing_address_1]')
    apartment = (By.CSS_SELECTOR, 'input[id=billing_address_2]')
    city = (By.CSS_SELECTOR, 'input[id=billing_city]')
    state = (By.CSS_SELECTOR, 'select[id=billing_state]')
    postal_code = (By.CSS_SELECTOR, 'input[id=billing_postcode]')
    phone = (By.CSS_SELECTOR, '#billing_phone')
    billing_mail = (By.CSS_SELECTOR, 'billing_email')
    account_username = (By.CSS_SELECTOR, '#account_username')
    account_password = (By.CSS_SELECTOR, '#account_password')
    show_password = (By.CSS_SELECTOR, '.show-password-input')
    newsletter_check_box = (By.CSS_SELECTOR, '#ce4wp_checkout_consent_checkbox')
    place_order = (By.CSS_SELECTOR, '#place_order')




