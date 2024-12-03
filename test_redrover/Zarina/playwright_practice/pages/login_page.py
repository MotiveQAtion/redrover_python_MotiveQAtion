from playwright.sync_api import Page

from test_redrover.Zarina.playwright_practice.data.urls import *


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator('#id_username')
        self.password_input = page.locator('#id_password')
        self.login_button = page.locator('//button[@type="submit"]')

    def navigate(self):
        """Открывает страницу логина."""
        self.page.goto(LOGIN_URL)

    def login(self, username: str, password: str):
        """Выполняет вход с заданными учетными данными."""
        self.username_input.fill("ZarUmb")
        self.password_input.fill("Miras110589")
        self.login_button.click()