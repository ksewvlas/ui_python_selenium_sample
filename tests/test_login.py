import allure
import pytest


@allure.description("Test successful login")
@pytest.mark.parametrize(
    'username, password',
    [
        ('standard_user', 'secret_sauce'),
        ('problem_user', 'secret_sauce'),
        ('performance_glitch_user', 'secret_sauce'),
    ],
)
def test_successful_login(login_page, main_page, username, password):
    login_page.input_user_name(username)
    login_page.input_password(password)
    login_page.click_login_button()
    title = main_page.get_title_word()

    assert title.text == 'Products', f'Title is not correct: {title.text}'


@allure.description("Test invalid login with incorrect username/password")
@pytest.mark.parametrize(
    'username, password',
    [
        ('standard_user', 'incorrect_password'),
        ('incorrect_username', 'secret_sauce'),
    ],
)
def test_incorrect_username_or_password(login_page, username, password):
    login_page.input_user_name(username)
    login_page.input_password(password)
    login_page.click_login_button()
    error_message = login_page.get_error_message()

    assert (
        error_message.text == 'Epic sadface: Username and password do not match '
        'any user in this service'
    ), 'Error message is not correct'


@allure.description("Test invalid login with empty username")
@pytest.mark.parametrize(
    'username, password',
    [
        ('', 'secret_sauce'),
    ],
)
def test_empty_username(login_page, username, password):
    login_page.input_user_name(username)
    login_page.input_password(password)
    login_page.click_login_button()
    error_message = login_page.get_error_message()

    assert (
        error_message.text == 'Epic sadface: Username is required'
    ), 'Error message is not correct'


@allure.description("Test invalid login with empty password")
@pytest.mark.parametrize('username, password', [('standard_user', '')])
def test_empty_password(login_page, username, password):
    login_page.input_user_name(username)
    login_page.input_password(password)
    login_page.click_login_button()
    error_message = login_page.get_error_message()

    assert (
        error_message.text == 'Epic sadface: Password is required'
    ), 'Error message is not correct'


@allure.description("Test invalid login with locked user")
@pytest.mark.parametrize('username, password', [('locked_out_user', 'secret_sauce')])
def test_locked_user(login_page, username, password):
    login_page.input_user_name(username)
    login_page.input_password(password)
    login_page.click_login_button()
    error_message = login_page.get_error_message()

    assert (
        error_message.text == 'Epic sadface: Sorry, this user has been locked out.'
    ), 'Error message is not correct'
