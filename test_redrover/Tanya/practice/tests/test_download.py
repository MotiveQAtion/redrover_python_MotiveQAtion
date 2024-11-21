import time

import allure

from test_redrover.Tanya.practice.pages.download_page import DownloadPage
from test_redrover.Tanya.practice.data.urls import Urls


class TestDownload:
    url = Urls()

    def test_download(self, browser):
        page = DownloadPage(browser, f"{self.url.herokuapp_base_url}download")
        page.open()
        page.download_file()
