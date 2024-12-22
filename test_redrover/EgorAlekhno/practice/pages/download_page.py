from test_redrover.EgorAlekhno.practice.locators.download_page_herokuapp_locators import DownLoadPageLocators
from test_redrover.EgorAlekhno.practice.pages.base_page import BasePage


class DownLoadPage(BasePage):
    locators = DownLoadPageLocators()

    def download_file(self):
        self.element_is_visible(self.locators.DOWNLOAD_LOCATOR).click()
