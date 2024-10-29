from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()


class WebElementWrapper:
    def __init__(self, element):
        self.element = element

    def should_be_visible(self):
        """Проверяет, виден ли элемент на странице."""
        if not self.element.is_displayed():
            raise AssertionError("Элемент не виден")


class Browser:
    def __init__(self, browser):
        self.browser = browser

    def open(self, url):
        self.browser.get(url)

    def element_with_xpath(self, xpath):
        """Находит элемент по XPATH и возвращает завернутый элемент."""
        try:
            element = self.browser.find_element(By.XPATH, xpath)
            return WebElementWrapper(element)
        except NoSuchElementException:
            raise AssertionError(f"Элемент с XPATH '{xpath}' не найден")


browser = Browser(driver)

browser.open("http://195.133.27.184/")
browser.element_with_xpath("//a[@href='/3/']").should_be_visible()
