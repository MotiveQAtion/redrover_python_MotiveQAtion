import time

from test_redrover.EgorAlekhno.practice.data.urls import Urls
from test_redrover.EgorAlekhno.practice.functions import get_root_path
from test_redrover.EgorAlekhno.practice.pages.upload_page import UploadPage


class TestUpload:
    url = Urls()

    def test_upload(self, driver):
        file_path = get_root_path("data/upload/luminoslogo.png")
        page = UploadPage(driver, f"{self.url.herokuapp_base_url}upload")
        page.open()
        page.upload_file(file_path)
        h3_text, file_name_text = page.check_upload_file()
        assert  h3_text == "File Uploaded!"
        assert  file_name_text == "luminoslogo.png"
        time.sleep(3)
