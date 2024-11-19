import pytest
from components.header import Header
from components.register import Register
from playwright.sync_api import Page
import allure


# Inspired by: https://gist.github.com/mgaitan/652d39a7df5076e38239d2ae3f6862ed
# @pytest.fixture(scope="session")
# def storage(tmp_path_factory):
#     return tmp_path_factory.mktemp("session") / "state.json"
# @pytest.fixture
# def page(new_context, storage):
#     if storage.exists():
#         yield new_context(storage_state=storage).new_page()
#     else:
#         context = new_context()
#         page = context.new_page()
#         # логика для авторизации
#         yield page
#         context.storage_state(path=storage)

@pytest.fixture
def header(page: Page):
    return Header(page)


@pytest.fixture
def register(page: Page):
    return Register(page)


@pytest.fixture(scope="function", autouse=True)
def video_and_screenshot(page: Page):
    yield  # здесь выполняется тест
    # Сохранить скриншот
    screenshot = page.screenshot()
    allure.attach(
        screenshot,
        name="screenshot",
        attachment_type=allure.attachment_type.PNG,
    )
    # Сохранить видео
    video = page.video.path()
    page.context.close()  # Закрыть контекст, чтобы видео сохранилось на диск
    allure.attach.file(
        video,
        name="video",
        attachment_type=allure.attachment_type.WEBM,
    )