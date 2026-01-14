import time
import allure
from playwright.sync_api import expect
import pytest

@allure.parent_suite("Testy automatyczne Product Store")
@allure.suite("Rejestracja użytkownika")
class TestLogin:
    field_wrong_credentials = [("invalidUser1", "invalidPass", "User does not exist."), ("invalidUser", "invalidPass", "Wrong password."), ("", "somePass", "Please fill out Username and Password."), ("someUser", "", "Please fill out Username and Password.")]

    @allure.title("Przypadek 01 - Logowanie poprawnymi danymi")
    @allure.description("Test służy sprawdzeniu czy wpisując dane prawidłowe zostanie użytkownik zalogowany")
    def test_login_success(self):
        username = "admin"
        password = "admin"
        self.main_page.navigate()
        self.main_page.click_and_fill_login(username, password)
        expect(self.page.locator("a[id='nameofuser']")).to_have_text("Welcome admin")

    @pytest.mark.parametrize("username, password, expected_message", field_wrong_credentials)
    @allure.title("Przypadek 02 - Logowanie z nieprawidłowymi danymi")
    @allure.description("Test służy sprawdzeniu czy wpisując nieprawidłowe dane użytkownik dostanie informację o błędzie")
    def test_login_with_invalid_credentials(self, username, password, expected_message):
        self.main_page.navigate()
        self.main_page.click_and_fill_login(username, password)
        self.main_page.verify_alert_message(expected_message)