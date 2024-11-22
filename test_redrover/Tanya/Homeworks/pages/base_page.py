from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

from test_redrover.Tanya.Homeworks.locators.locators import LOGIN_BTN


class BasePage:
    def __init__(self, browser, BASE_URL):
        self.browser = browser
        self.url = BASE_URL

    def open(self):
        self.browser.get(self.url)

    def element_is_visible(self, locator, timeout=10):
        return wait(self.browser, timeout=timeout).until(EC.visibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=10):
        return wait(self.browser, timeout=timeout).until(EC.element_to_be_clickable(locator))

    def element_is_present(self, locator, timeout=10):
        return wait(self.browser, timeout=timeout).until(EC.presence_of_element_located(locator))

    def click_to_element(self, locator):
        return self.element_is_clickable(locator).click()

    # def click_login_btn(browser):
    #     login_btn = browser.find_element(LOGIN_BTN)
    #     login_btn.click()
