from logging import getLogger

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.page import Page


logger = getLogger(__name__)


class LoginPage(Page):
    url = "https://www.saucedemo.com/"

    # Locators
    user_name = '//input[@data-test="username"]'
    password = '//input[@data-test="password"]'
    login_button = '//input[@data-test="login-button"]'
    error_message = '//h3[@data-test="error"]'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Getters
    def get_user_name(self):
        """
        Get field for username.

        :return:
        """
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.user_name))
        )

    def get_password(self):
        """
        Get field for password.

        :return:
        """
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.password))
        )

    def get_login_button(self):
        """
        Get login button

        :return:
        """
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.login_button))
        )

    def get_error_message(self):
        """
        Get error message

        :return:
        """
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.error_message))
        )

    # Actions
    def input_user_name(self, user_name):
        """
        Input username in the username field.

        :param user_name: existing username.
        """

        self.get_user_name().send_keys(user_name)

    def input_password(self, password):
        """
        Input password in the password field

        :param password: correct password
        """
        self.get_password().send_keys(password)

    def click_login_button(self):
        """
        Click on the login button.
        """
        self.get_login_button().click()

    # Methods
    @allure.step('Authorization')
    def authorization(self):
        logger.info('Make an Authorization')
        self.get_current_url()
        self.input_user_name('standard_user')
        self.input_password('secret_sauce')
        self.click_login_button()
