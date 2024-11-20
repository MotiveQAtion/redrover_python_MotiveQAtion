from test_redrover.Tanya.practice.pages.base_page import BasePage
from test_redrover.Tanya.practice.locators.upload_page_herokuapp_locator import UploadPageLocators


class UploadPage(BasePage):
    locators = UploadPageLocators()

    def upload_file(self, file_path):
        self.element_is_visible(self.locators.CHOOSE_FILE_BTN).send_keys(file_path)
        self.element_is_clickable(self.locators.SUBMIT_BTN).click()

    def check_upload_file(self):
        h3_text = self.element_is_visible(self.locators.HEADER_TEXT_LOCATOR).text
        file_name_text = self.element_is_visible(self.locators.UPLOAD_FILE_NAME_LOCATOR).text
        return h3_text, file_name_text
