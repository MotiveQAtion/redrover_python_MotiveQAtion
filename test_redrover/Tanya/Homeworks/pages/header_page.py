from test_redrover.Tanya.Homeworks.locators.locators import LOGIN_BTN
from test_redrover.Tanya.Homeworks.pages.base_page import BasePage
from test_redrover.Tanya.Homeworks.pages.login_page import LoginPage


class Header(BasePage):

    def click_login_btn(self):
        self.click_to_element(LOGIN_BTN)
        return LoginPage
