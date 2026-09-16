import pytest
from playwright.sync_api import Page

from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


@pytest.fixture
def login_page(page: Page, settings):
    login = LoginPage(page, settings.ui_base_url)
    login.open()
    return login


@pytest.mark.ui
@pytest.mark.external
@pytest.mark.smoke
def test_standard_user_can_open_inventory(login_page, settings):
    login_page.login(settings.sauce_username, settings.sauce_password)

    InventoryPage(login_page.page, settings.ui_base_url).expect_loaded()


@pytest.mark.ui
@pytest.mark.external
@pytest.mark.regression
def test_invalid_login_shows_actionable_error(login_page):
    login_page.login("standard_user", "wrong-password")

    login_page.expect_error("Username and password do not match")


@pytest.mark.ui
@pytest.mark.external
@pytest.mark.regression
def test_user_can_add_backpack_to_cart(login_page, settings):
    login_page.login(settings.sauce_username, settings.sauce_password)
    inventory = InventoryPage(login_page.page, settings.ui_base_url)
    inventory.expect_loaded()
    inventory.add_backpack()
    inventory.open_cart()

    CartPage(login_page.page, settings.ui_base_url).expect_item("Sauce Labs Backpack")

