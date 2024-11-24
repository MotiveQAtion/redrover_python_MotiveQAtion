# login_page.py
from playwright.sync_api import Page
from tests_tutors_web.config import WEB_USERNAME, WEB_PASSWORD, T_PASSWORD, T_NAME
from tests_PW_tutor_platform.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page):
        self.page = page
        self.username_input = '#id_username'
        self.password_input = '#id_password'
        self.submit_button = '//button[@type="submit"]'
        # self.dashboard_selector = ''  # Замените на реальный селектор после входа

    def login(self, username: str, password: str):
        self.page.locator(self.username_input).fill(username)
        self.page.locator(self.password_input).fill(password)
        self.page.click(self.submit_button)
        return BasePage
        # Ожидание успешного входа
        # self.page.locator(self.dashboard_selector).wait_for()
