import logging
import allure

class MainPage:        
    def __init__(self, page):
        self.page = page
        self.logger = logging.getLogger(__name__)
        
    @allure.step("Navigating to Product Store home page")
    def navigate(self):
        self.page.goto("https://www.demoblaze.com/index.html")
        self.logger.info("Navigated to Product Store home page")

    @allure.step(f"Clicking Sign Up button and filling the form - {1}")
    def click_and_fill_sign_up(self, username, password):
        self.page.get_by_role("link", name="Sign up").click()
        self.page.get_by_role("textbox", name="Username:").fill(username)
        self.page.get_by_role("textbox", name="Password:").fill(password)
        self.page.get_by_role("button", name="Sign up").click()
        self.logger.info("Sigh up form filled and submitted")
    
    @allure.step("Verifying alert message - {1}")
    def verify_alert_message(self, expected_message):   
        alert = self.page.wait_for_event("dialog")
        assert alert.message == expected_message, f"Expected alert message '{expected_message}', but got '{alert.message}'"
        alert.accept()
        self.logger.info(f"Alert message verified: {expected_message}")