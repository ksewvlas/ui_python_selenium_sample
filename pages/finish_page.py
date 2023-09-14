import allure
from logging import getLogger

from base.page import Page


logger = getLogger(__name__)


class FinishPage(Page):
    # Locators

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Getters

    # Actions

    # Methods
    @allure.step('Screenshot')
    def screenshot(self):
        logger.info('Create a screenshot')
        self.get_current_url()
        self.create_screenshot()
