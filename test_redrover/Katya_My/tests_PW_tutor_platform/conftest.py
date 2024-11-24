import pytest
from playwright.sync_api import sync_playwright, Page
from tests_tutors_web.config import WEB_USERNAME, WEB_PASSWORD, T_PASSWORD, T_NAME
from tests_PW_tutor_platform.pages.login_page import LoginPage
from tests_PW_tutor_platform.base_page import BasePage

WEB_URL = 'http://195.133.27.184/login/'


# from tests_PW_tutor_platform.pages.playwright_languages_page import PlaywrightLanguagesPage

@pytest.fixture(scope="session")
def browser_fixture():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        page.close()
        browser.close()


'пример использования фикстуры для изменения  размера браузера'


@pytest.fixture()
def login_student(page: Page):
    login_page = LoginPage(page)
    login_page.load(WEB_URL)
    login_page.login(WEB_USERNAME, WEB_PASSWORD)
    # Возвращаем объект Page после успешного входа
    return page


@pytest.fixture()
def login_tutors(page: Page):
    login_page = LoginPage(page)
    login_page.load(WEB_URL)
    login_page.login(T_NAME, T_PASSWORD)
    return page


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {

        "viewport": {
            "width": 1920,
            "height": 1080,
        }
    }

# '''Или установить cookies. Имена и параметры нужно передавать как массив словарей'''
#
# @pytest.fixture(scope="session")
# def browser_context_args(browser_context_args):
#     return {
#         **browser_context_args,
#         "storage_state": {
#             "cookies": [
#                 {
#                     "name": "stepik",
#                     "value": "sd4fFfv!x_cfcstepik",
#                     "url": "https://example.com"  # Замените на нужный URL
#                 },
#             ]
#         },
#     }
