from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=10):
        return wait(self.driver, timeout=timeout).until(EC.visibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=10):
        return wait(self.driver, timeout=timeout).until(EC.element_to_be_clickable(locator))

    def element_is_present(self, locator, timeout=10):
        return wait(self.driver, timeout=timeout).until(EC.presence_of_element_located(locator))
    def alert_is_visible(self, timeout=10):
        wait(self.driver, timeout=timeout).until(EC.alert_is_present())
