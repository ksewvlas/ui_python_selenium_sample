from datetime import datetime

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Page:
    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        """
        Get current url.

        :return: current url.
        """
        return self.driver.current_url

    def create_screenshot(self):
        """
        Create a screenshot
        """
        now_date = datetime.utcnow().strftime('%Y.%m.%d.%H.%M.%S')
        screenshot_name = f'./screen/screenshot-{now_date}.png'
        return self.driver.save_screenshot(screenshot_name)

    def is_expected_url(self, expected_url):
        """
        Compare two urls.

        :param expected_url: expected url, str
        :raises AssertionError: if urls are not the same
        """
        if self.driver.current_url == expected_url:
            return True
        return False

    def is_element_visible(self, by, locator: str, timeout=15):
        try:
            element = WebDriverWait(self, timeout).until(
                EC.visibility_of_element_located((by, locator))
            )
            return element.is_displayed()
        except Exception:
            return False
