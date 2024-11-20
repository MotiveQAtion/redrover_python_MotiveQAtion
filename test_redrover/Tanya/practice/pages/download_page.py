from test_redrover.Tanya.practice.pages.base_page import BasePage
from test_redrover.Tanya.practice.locators.dounload_page_herokuapp_locator import DownloadPageLocators


class DownloadPage(BasePage):
    locators = DownloadPageLocators()

    def download_file(self):
        self.element_is_visible(self.locators.DOWNLOAD_LOC).click()
