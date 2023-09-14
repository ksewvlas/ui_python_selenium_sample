import allure


@allure.description("Test go to about link")
def test_go_to_about_link(login_and_goto_main):
    login_and_goto_main.select_menu_about()

    assert login_and_goto_main.is_expected_url(
        expected_url="https://saucelabs.com/"
    ), f'Url does not match: {login_and_goto_main.get_current_url()}'


@allure.description("Test go to all items")
def test_go_to_all_items(login_and_goto_main):
    login_and_goto_main.select_menu_all_items()

    assert login_and_goto_main.is_expected_url(
        expected_url="https://www.saucedemo.com/inventory.html"
    ), f'Url does not match: {login_and_goto_main.get_current_url()}'
