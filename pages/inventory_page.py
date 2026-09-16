from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class InventoryPage(BasePage):
    def __init__(self, page: Page, base_url: str) -> None:
        super().__init__(page, base_url)
        self.cart_link = page.get_by_test_id("shopping-cart-link")

    def expect_loaded(self) -> None:
        expect(self.page).to_have_url("**/inventory.html")
        expect(self.page.get_by_text("Products")).to_be_visible()

    def add_backpack(self) -> None:
        self.page.get_by_test_id("add-to-cart-sauce-labs-backpack").click()

    def open_cart(self) -> None:
        self.cart_link.click()

