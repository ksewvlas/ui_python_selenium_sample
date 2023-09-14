from logging import getLogger

import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from base.page import Page


logger = getLogger(__name__)


class CartPage(Page):
    # Locators
    checkout_button = '//button[@data-test="checkout"]'
    cart_items = '//div[@class="cart_item"]'
    cart_item_name = './/div[@class="inventory_item_name"]'
    cart_item_price = './/div[@class="inventory_item_price"]'
    cart_item_add_button = './/button[contains(@class, "cart_button")]'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Getters
    def get_checkout_button(self):
        """
        Get element Checkout Button.

        :return: element
        """
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.checkout_button))
        )

    def get_cart_items(self):
        """
        Get cart items on the page.

        :return: list of elements
        """
        return self.driver.find_elements(By.XPATH, self.cart_items)

    def get_cart_item(self, index: int = 0):
        """
        Get cart item by its index.
        By default, returns the first element.

        :param index: specify the index of cart item(by default, 0)
        :return: the n item of cart
        :raises: IndexError if index is not found in the list of items.
        """
        return self.get_cart_items()[index]

    def get_cart_item_button(self, index: int = 0):
        """
        Get cart item button by its index.
        By default, returns the button of the first element.

        :param index: specify the index of cart item(by default, 0)
        :return: the n item button of cart
        :raises: IndexError if index is not found in the list of items.
        """
        cart_item = self.get_cart_item(index)
        return WebDriverWait(cart_item, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.cart_item_add_button))
        )

    def get_cart_item_name(self, index: int = 0):
        """
        Get cart item name by its index.
        By default, returns the name of the first element.

        :param index: specify the index of cart item(by default, 0)
        :return: the n item name of cart
        :raises: IndexError if index is not found in the list of items.
        """
        cart_item = self.get_cart_item(index)
        return WebDriverWait(cart_item, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.cart_item_name))
        )

    def get_cart_item_price(self, index: int = 0):
        """
        Get cart item price by its index.
        By default, returns the price of the first element.

        :param index: specify the index of cart item(by default, 0)
        :return: the n item price of cart
        :raises: IndexError if index is not found in the list of items.
        """
        final_item = self.get_cart_item(index)
        return WebDriverWait(final_item, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.cart_item_price))
        )

    # Actions
    def click_checkout_button(self):
        """
        Click on the checkout button.
        """
        self.get_checkout_button().click()

    # Methods
    @allure.step('Product confirmation')
    def product_confirmation(self):
        logger.info('Confirm a product')
        self.get_current_url()
        self.click_checkout_button()

    def is_product_in_cart(self, product_name):
        cart_items = self.get_cart_items()

        for item in cart_items:
            item_name = item.find_element(By.XPATH, self.cart_item_name).text

            if item_name == product_name:
                return True

        return False

    def are_products_in_cart(self, added_products):
        mismatched_products = []
        cart_items = self.get_cart_items()

        for item in cart_items:
            item_name = item.find_element(By.XPATH, self.cart_item_name).text
            item_price = item.find_element(By.XPATH, self.cart_item_price).text

            if (
                item_name not in added_products
                or item_price != added_products[item_name]
            ):
                mismatched_products.append(item_name)

        return not bool(mismatched_products), mismatched_products
