from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def element_is_visible(self, locator, timeout=10):
        return wait(self.browser, timeout=timeout).until(EC.visibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=10):
        return wait(self.browser, timeout=timeout).until(EC.element_to_be_clickable(locator))

    def element_is_present(self, locator, timeout=10):
        return wait(self.browser, timeout=timeout).until(EC.presence_of_element_located(locator))
