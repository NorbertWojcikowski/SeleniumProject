from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPageLocators:
    CREATE_AN_ACCOUNT_BUTTON = (By.XPATH, '//a[@class="btn"]')
    EMAIL_INPUT = (By.XPATH, '//input[@name="email_address"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@name="password"]')
    SIGN_IN_BUTTON = (By.XPATH, '//button[@class="btn btn-login btn-second"]')
    LOGIN_ERRORS = (By.XPATH, '//div[@class="messageStackError"]/ul/li')


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def click_registration_account_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginPageLocators.CREATE_AN_ACCOUNT_BUTTON)).click()

    def entering_email(self, email):
        email_input = self.driver.find_element(*LoginPageLocators.EMAIL_INPUT)
        email_input.send_keys(email)

    def entering_password(self, password):
        password_input = self.driver.find_element(*LoginPageLocators.PASSWORD_INPUT)
        password_input.send_keys(password)

    def click_sign_in_button(self):
        sign_in_button = self.driver.find_element(*LoginPageLocators.SIGN_IN_BUTTON)
        sign_in_button.click()

    def error_message(self, expected_error):
        errors = self.driver.find_elements(*LoginPageLocators.LOGIN_ERRORS)
        errors_texts = []
        for e in errors:
            errors_texts.append(e.text)
        assert errors_texts[0] == expected_error

    def no_password_entered_message(self, expected_error):
        message = self.driver.find_element(*LoginPageLocators.PASSWORD_INPUT).get_attribute("validationMessage")
        assert message == expected_error
