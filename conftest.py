import allure
import pytest

from Pages.mainPage import MainPage


@pytest.fixture(scope="function", autouse=True)
def setup_pages(page, request):
    """
    Fixture dla całej klasy testowej.
    Tworzy instancje wszystkich potrzebnych Page Object.
    """
    request.cls.page = page
    request.cls.main_page = MainPage(page)

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    if result.when == "call" and result.failed:
        if "page" in item.fixturenames:
            page = item.funcargs["page"]
            png = page.screenshot()
            allure.attach(
                png, name="screenshot", attachment_type=allure.attachment_type.PNG
            )
