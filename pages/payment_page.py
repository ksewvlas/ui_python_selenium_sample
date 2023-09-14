import allure
from logging import getLogger

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from base.page import Page


logger = getLogger(__name__)


class PaymentPage(Page):
    # Locators
    finish_button = '//button[@data-test="finish"]'
    final_items = '//div[@class="cart_item"]'
    final_item_name = './/div[@class="inventory_item_name"]'
    final_item_price = './/div[@class="inventory_item_price"]'
    items_total_price = '//div[@class="summary_subtotal_label"]'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Getters
    def get_finish_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.finish_button))
        )

    def get_final_items(self):
        return self.driver.find_elements(By.XPATH, self.final_items)

    def get_final_item(self, index=0):
        return self.get_final_items()[index]

    def get_final_item_name(self, index=0):
        final_item = self.get_final_item(index)
        return WebDriverWait(final_item, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.final_item_name))
        )

    def get_final_item_price(self, index=0):
        final_item = self.get_final_item(index)
        return WebDriverWait(final_item, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.final_item_price))
        )

    def get_items_total_price(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.items_total_price))
        )

    def click_finish_button(self):
        self.get_finish_button().click()

    # Methods
    @allure.step('Make payment')
    def make_payment(self):
        logger.info('Make payment')
        self.get_current_url()
        self.click_finish_button()

    def sum_final_items_price(self):
        price = 0
        for element in range(len(self.get_final_items())):
            price += float(self.get_final_item_price(element).text[1:])
        return price
