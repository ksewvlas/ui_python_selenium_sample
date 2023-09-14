from random import randint

import allure
import pytest


@allure.description("Test add a one product to cart")
@pytest.mark.parametrize('product_index', [randint(0, 5) for _ in range(3)])
def test_add_one_product_to_cart(login_and_goto_main, cart_page, product_index):
    product_name = login_and_goto_main.get_product_name(index=product_index).text
    product_price = login_and_goto_main.get_product_price(index=product_index).text
    login_and_goto_main.select_product(index=product_index)
    final_quantity = login_and_goto_main.get_cart_item_quantity().text
    cart_item_name = cart_page.get_cart_item_name().text
    cart_item_price = cart_page.get_cart_item_price().text

    assert (
        int(final_quantity) == 1
    ), f'Expected cart item quantity to be 1, but got {final_quantity}'
    assert cart_page.is_product_in_cart(
        product_name
    ), f'The product "{product_name}" is not in the cart'
    assert (
        product_name == cart_item_name
    ), f'The product names are not equals: {product_name} != {cart_item_name}'
    assert (
        product_price == cart_item_price
    ), f'The product prices are not equals: {product_price} != {cart_item_price}'


@allure.description("Test add some products to cart")
@pytest.mark.parametrize('quantity_products', [randint(1, 6)])
def test_add_some_products_to_cart(login_and_goto_main, cart_page, quantity_products):
    added_product_indexes = login_and_goto_main.select_random_products(
        quantity_products
    )
    added_products = dict()

    for product_index in added_product_indexes:
        product_name = login_and_goto_main.get_product_name(index=product_index).text
        product_price = login_and_goto_main.get_product_price(index=product_index).text
        added_products[product_name] = product_price
        login_and_goto_main.click_product_add_button(index=product_index)

    quantity_cart_items = login_and_goto_main.get_cart_item_quantity().text
    login_and_goto_main.click_cart()

    assert int(quantity_cart_items) == quantity_products
    assert cart_page.are_products_in_cart(
        added_products
    ), f'Products do not match: {added_products}'
