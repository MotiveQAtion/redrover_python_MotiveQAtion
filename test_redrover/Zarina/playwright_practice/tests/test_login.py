from playwright.sync_api import expect
from test_redrover.Zarina.playwright_practice.data.urls import *
from test_redrover.Zarina.playwright_practice.pages.login_page import LoginPage


def test_login(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("ZarUmb","Miras110589")
    expect(page).to_have_url(LOGIN_DONE_URL)