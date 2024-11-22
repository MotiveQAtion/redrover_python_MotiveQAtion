import time

from test_redrover.Tanya.Homeworks.pages.login_page import LoginPage
from test_redrover.Tanya.Homeworks.data.urls import BASE_URL
from test_redrover.Tanya.Homeworks.pages.header_page import Header


class TestLogin:
    def test_login(self, browser):
        page = LoginPage(browser, BASE_URL)
        page.open()
        header = Header(browser, BASE_URL)
        header.click_login_btn()
        time.sleep(3)
        page.check_login()
        time.sleep(3)
