from random import randint

import allure


@allure.description("Test buy product")
def test_buy_product(
    login_page, main_page, cart_page, client_information_page, payment_page, finish_page
):
    login_page.authorization()
    main_page_title = main_page.get_title_word().text

    random_product_number = randint(0, len(main_page.get_products()) - 1)
    initial_product_name = main_page.get_product_name(index=random_product_number).text
    initial_product_price = main_page.get_product_price(
        index=random_product_number
    ).text
    main_page.select_product(index=random_product_number)

    cart_item_name = cart_page.get_cart_item_name().text
    cart_item_price = cart_page.get_cart_item_price().text

    cart_page.product_confirmation()
    client_information_page.fill_information()

    payment_item_name = payment_page.get_final_item_name().text
    payment_item_price = payment_page.get_final_item_price().text
    final_items_price = payment_page.sum_final_items_price()
    items_total_price = payment_page.get_items_total_price().text.split("$")[1]

    payment_page.make_payment()
    finish_page.screenshot()

    assert main_page_title == "Products"
    assert cart_item_name == initial_product_name
    assert cart_item_price == initial_product_price
    assert payment_item_name == initial_product_name
    assert payment_item_price == initial_product_price
    assert float(items_total_price) == final_items_price
    assert finish_page.is_expected_url(
        expected_url="https://www.saucedemo.com/checkout-complete.html"
    )
