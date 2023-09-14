from logging import getLogger

import pytest
from selenium import webdriver

from pages.main_page import MainPage
from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.finish_page import FinishPage
from pages.payment_page import PaymentPage
from pages.client_information_page import ClientInformationPage


logger = getLogger(__name__)


@pytest.fixture(autouse=True)
def log_test_start_and_end(request):
    test_name = request.node.name
    logger.info(f"Starting test: {test_name}")
    yield
    logger.info(f"Finished test: {test_name}")


@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("-headless=new")
    driver = webdriver.Chrome(options=options)
    url = "https://www.saucedemo.com/"
    driver.get(url=url)
    driver.fullscreen_window()
    yield driver  # here execute test
    driver.quit()


@pytest.fixture()
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture()
def main_page(driver):
    return MainPage(driver)


@pytest.fixture()
def cart_page(driver):
    return CartPage(driver)


@pytest.fixture()
def client_information_page(driver):
    return ClientInformationPage(driver)


@pytest.fixture()
def payment_page(driver):
    return PaymentPage(driver)


@pytest.fixture()
def finish_page(driver):
    return FinishPage(driver)


@pytest.fixture()
def login_and_goto_main(driver, login_page):
    login_page.authorization()
    return MainPage(driver)
