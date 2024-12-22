import time

from test_redrover.EgorAlekhno.practice.data.urls import Urls
from test_redrover.EgorAlekhno.practice.pages.download_page import DownLoadPage


class TestDownload:
    url = Urls()

    def test_download(self, driver):
        page = DownLoadPage(driver, f"{self.url.herokuapp_base_url}download")
        page.open()
        page.download_file()
        time.sleep(5)
