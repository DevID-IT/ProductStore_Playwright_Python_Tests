import allure
from faker import Faker
import pytest


@allure.parent_suite("Testy automatyczne Product Store")
@allure.suite("Rejestracja użytkownika")
class TestSignUp:
    field_missing_credentials = [("", ""), ("Dawid6286", ""), ("", "Dawid6286")]
    
    def setup_method(self):
        self.faker = Faker()
        
    
    @allure.title("Przypadek 01 - Rejestracja poprawnymi danymi")
    @allure.description("Test służy sprawdzeniu czy wpisując dane prawidłowe zostanie użytkownik zarejestrowany")
    def test_register_success(self):
        username = self.faker.user_name()
        password = self.faker.password()
        self.main_page.navigate()
        self.main_page.click_and_fill_sign_up(username, password)
        self.main_page.verify_alert_message("Sign up successful.")



    @allure.title("Przypadek 02 - Rejestracja z istniejącym loginem")
    @allure.description("Test służy sprawdzeniu czy wpisując istniejący login użytkownik dostanie informację o błędzie")
    def test_register_with_existing_username(self):
        existing_username = "admin"
        password = self.faker.password()
        self.main_page.navigate()
        self.main_page.click_and_fill_sign_up(existing_username, password)
        self.main_page.verify_alert_message("This user already exist.")

    @pytest.mark.parametrize("username, password", field_missing_credentials)
    @allure.title("Przypadek 03 - Rejestracja z pustymi polami")
    @allure.description("Test służy sprawdzeniu czy wszystkie pola obowiązkowe są sprawdzane podczas rejestracji")
    def test_register_validation(self, username, password):
        self.main_page.navigate()
        self.main_page.click_and_fill_sign_up(username, password)
        self.main_page.verify_alert_message("Please fill out Username and Password.")