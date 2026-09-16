from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, page: Page, base_url: str) -> None:
        super().__init__(page, base_url)

    def expect_item(self, item_name: str) -> None:
        expect(self.page.get_by_text(item_name)).to_be_visible()

