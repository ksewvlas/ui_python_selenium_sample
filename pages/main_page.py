from random import choice
from logging import getLogger

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.page import Page


logger = getLogger(__name__)


class MainPage(Page):
    # Locators
    title_word = '//span[@class="title"]'
    products = '//div[@class="inventory_item"]'
    product_name = './/div[@class="inventory_item_name"]'
    product_price = './/div[@class="inventory_item_price"]'
    product_add_button = './/button[contains(@class, "btn_inventory")]'
    cart = '//div[@id="shopping_cart_container"]'
    cart_item_quantity = '//span[@class="shopping_cart_badge"]'
    menu_button = '//button[@id="react-burger-menu-btn"]'
    about_link = '//a[@id="about_sidebar_link"]'
    all_items_link = '//a[@id="inventory_sidebar_link"]'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Getters
    def get_title_word(self):
        """
        Get element title.

        :return: element
        """
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.title_word))
        )

    def get_products(self):
        """
        Get elements of products

        :return: list of elements
        """
        return self.driver.find_elements(By.XPATH, self.products)

    def get_product(self, index: int = 0):
        """
        Get product by its index.
        By default, returns the first element.

        :param index: specify the index of product(by default, 0)
        :return: the n product
        :raises: IndexError if index is not found in the list of items.
        """
        products = self.get_products()
        if not (0 <= index < len(products)):
            raise IndexError(
                f"Invalid product index: {index}. Number of products available: {len(products)}"
            )
        return products[index]

    def get_product_name(self, index: int = 0):
        """
        Get product name by its index.
        By default, returns the name of the first element.

        :param index: specify the index of product(by default, 0)
        :return: the n product name
        :raises: IndexError if index is not found in the list of items.
        """
        product = self.get_product(index)
        return WebDriverWait(product, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.product_name))
        )

    def get_product_price(self, index: int = 0):
        """
        Get product price by its index.
        By default, returns the price of the first element.

        :param index: specify the index of product(by default, 0)
        :return: the n product price
        :raises: IndexError if index is not found in the list of items.
        """
        final_item = self.get_product(index)
        return WebDriverWait(final_item, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.product_price))
        )

    def get_product_add_button(self, index: int = 0):
        """
        Get product add button by its index.
        By default, returns the add button of the first element.

        :param index: specify the index of product(by default, 0)
        :return: the n product add button
        :raises: IndexError if index is not found in the list of items.
        """
        product = self.get_product(index)
        return WebDriverWait(product, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.product_add_button))
        )

    def get_cart(self):
        """
        Get cart

        :return: the cart
        """
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.cart))
        )

    def get_cart_item_quantity(self):
        """
        Get cart badge

        :return: the cart badge
        """
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.cart_item_quantity))
        )

    def get_menu_button(self):
        """
        Get element of the menu button

        :return: the menu button
        """
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.menu_button))
        )

    def get_about_link(self):
        """
        Get element of the link about

        :return: the about link
        """
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.about_link))
        )

    def get_all_items_link(self):
        """
        Get element of the link about

        :return: the about link
        """
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.all_items_link))
        )

    # Actions
    def click_product_add_button(self, index: int = 0):
        """
        Click on the product add button.

        :param index:
        """
        products = self.get_products()
        if 0 <= index < len(products):
            self.get_product_add_button(index).click()
        else:
            raise IndexError(f"Invalid product index: {index}")

    def click_cart(self):
        self.get_cart().click()

    def click_menu_button(self):
        self.get_menu_button().click()

    def click_about_link(self):
        self.get_about_link().click()

    def click_all_items_link(self):
        self.get_all_items_link().click()

    # Methods

    @allure.step('Select product')
    def select_product(self, index: int = 0):
        logger.info('Select a product')
        self.get_current_url()
        self.click_product_add_button(index)
        self.click_cart()

    @allure.step('Select menu about')
    def select_menu_about(self, make_screenshot=False):
        logger.info('Select a link About')
        self.get_current_url()
        self.click_menu_button()
        self.click_about_link()
        if make_screenshot:
            self.create_screenshot()

    @allure.step('Select menu all items')
    def select_menu_all_items(self, make_screenshot=False):
        logger.info('Select a link All items')
        self.get_current_url()
        self.click_menu_button()
        self.click_all_items_link()
        if make_screenshot:
            self.create_screenshot()

    def select_random_products(self, quantity):
        available_product_indexes = list(range(0, 6))
        selected_indexes = set()

        for _ in range(quantity):
            available_indices = [
                i for i in available_product_indexes if i not in selected_indexes
            ]
            if not available_indices:
                break
            product_index = choice(available_indices)
            selected_indexes.add(product_index)

        return selected_indexes
