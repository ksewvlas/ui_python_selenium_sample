from faker import Faker
import allure
from logging import getLogger

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from base.page import Page

logger = getLogger(__name__)

fake = Faker()


class ClientInformationPage(Page):
    # Locators
    first_name = '//input[@data-test="firstName"]'
    last_name = '//input[@data-test="lastName"]'
    postal_code = '//input[@data-test="postalCode"]'
    continue_button = '//input[@data-test="continue"]'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Getters
    def get_first_name(self):
        """
        Get field for first name.

        :return:
        """
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.first_name))
        )

    def get_last_name(self):
        """
        Get field for last name.

        :return:
        """
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.last_name))
        )

    def get_postal_code(self):
        """
        Get field postal code.

        :return:
        """
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.postal_code))
        )

    def get_continue_button(self):
        """
        Get continue button.

        :return:
        """
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.continue_button))
        )

    # Actions
    def input_first_name(self):
        """
        Input first name in the first name field.
        """
        first_name = fake.first_name()
        self.get_first_name().send_keys(first_name)

    def input_last_name(self):
        """
        Input last name in the last name field.
        """
        last_name = fake.last_name()
        self.get_last_name().send_keys(last_name)

    def input_postal_code(self):
        """
        Input postal code in the postal code field.
        """
        postal_code = fake.postalcode()
        self.get_postal_code().send_keys(postal_code)

    def click_continue_button(self):
        """
        Click on the continue button.
        """
        self.get_continue_button().click()

    # Methods
    @allure.step('Fill information')
    def fill_information(self):
        logger.info('Fill information about customer')
        self.get_current_url()
        self.input_first_name()
        self.input_last_name()
        self.input_postal_code()
        self.click_continue_button()
