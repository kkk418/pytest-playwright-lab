import re

from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class InventoryPage(BasePage):
    def __init__(self, page: Page, base_url: str) -> None:
        super().__init__(page, base_url)
        self.cart_link = page.locator('[data-test="shopping-cart-link"]')

    def expect_loaded(self) -> None:
        expect(self.page).to_have_url(re.compile(r".*/inventory\.html(?:\?.*)?\s*$"))
        expect(self.page.get_by_text("Products")).to_be_visible()

    def add_backpack(self) -> None:
        self.page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()

    def open_cart(self) -> None:
        self.cart_link.click()

