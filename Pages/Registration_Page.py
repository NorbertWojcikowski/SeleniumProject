from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RegistrationPageLocators:
    REGISTRATION_PAGE_TITLE = (By.XPATH, '//div[@class="content_head"]/h1')
    NAME_INPUT = (By.XPATH, '//input[@name="firstname"]')
    LAST_NAME_INPUT = (By.XPATH, '//input[@name="lastname"]')
    EMAIL_INPUT = (By.XPATH, '//input[@name="email"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@name="password"]')
    REPEAT_PASSWORD_INPUT = (By.XPATH, '//input[@name="confirmation"]')
    ACCEPT_THE_REGULATIONS_CHECKBOX = (By.ID, 'checkbox_reg_accept')
    SIGN_UP_BUTTON = (By.XPATH, '//button[@class="btn"]')
    REGISTRATION_ERRORS = (By.XPATH, '//span[@class="help-block form-error"]')


class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver

    def whether_registration_page_load_correctly(self, title):
        registration_title = self.driver.find_element(*RegistrationPageLocators.REGISTRATION_PAGE_TITLE)
        assert registration_title.text == title

    def entering_name(self, name):
        name_input = self.driver.find_element(*RegistrationPageLocators.NAME_INPUT)
        name_input.send_keys(name)

    def entering_last_name(self, last_name):
        last_name_input = self.driver.find_element(*RegistrationPageLocators.LAST_NAME_INPUT)
        last_name_input.send_keys(last_name)

    def entering_email(self, email):
        email_input = self.driver.find_element(*RegistrationPageLocators.EMAIL_INPUT)
        email_input.send_keys(email)

    def entering_password(self, password):
        password_input = self.driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT)
        password_input.send_keys(password)

    def entering_repeat_password(self, repeat_password):
        repeat_password_input = self.driver.find_element(*RegistrationPageLocators.REPEAT_PASSWORD_INPUT)
        repeat_password_input.send_keys(repeat_password)

    def mark_acceptance_of_the_regulations(self):
        mark_checkbox = self.driver.find_element(*RegistrationPageLocators.ACCEPT_THE_REGULATIONS_CHECKBOX)
        mark_checkbox.click()

    def click_create_customer_account(self):
        create_account_button = self.driver.find_element(*RegistrationPageLocators.SIGN_UP_BUTTON)
        create_account_button.click()

    def error_message(self, expected_error):
        errors = self.driver.find_elements(*RegistrationPageLocators.REGISTRATION_ERRORS)
        errors_texts = []
        for e in errors:
            errors_texts.append(e.text)
        if len(errors_texts) == 1:
            assert errors_texts[0] == expected_error
        else:
            print("There is more than 1 error")
