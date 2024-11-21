import time

from test_redrover.Tanya.practice.pages.upload_page import UploadPage
from test_redrover.Tanya.practice.data.urls import Urls
from test_redrover.Tanya.practice.functions import get_root_path


class TestUpload:
    url = Urls()

    def test_upload_file(self, browser):
        file_path = get_root_path("data/upload/sample_media_file.png")
        page = UploadPage(browser, f"{self.url.herokuapp_base_url}upload")
        page.open()
        page.upload_file(file_path)

        h3_text, file_name = page.check_upload_file()

        assert h3_text == "File Uploaded!"
        assert file_name == "sample_media_file.png"

