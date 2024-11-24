from playwright.sync_api import Page

from tests_PW_tutor_platform.base_page import BasePage


class PlaywrightHomePage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)