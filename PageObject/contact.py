from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class ContactPage:
    def __init__(self,driver):
        self.driver = driver

    call_us_now = (By.CSS_SELECTOR, '.elementor-button-link')
    name = (By.CSS_SELECTOR, '#evf-277-field_ys0GeZISRs-1')
    email = (By.CSS_SELECTOR, '#evf-277-field_LbH5NxasXM-2')
    phone = (By.CSS_SELECTOR, 'evf-277-field_66FR384cge-3')
    message =(By.CSS_SELECTOR, 'evf-277-field_yhGx3FOwr2-4')
    submit = (By.CSS_SELECTOR, '#evf-submit-277')
    scroll_to_top = (By.CSS_SELECTOR, 'tg-scroll-to-top')
