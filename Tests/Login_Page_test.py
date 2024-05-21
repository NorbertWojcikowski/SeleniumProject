from Pages.Home_Page import HomePage
from Tests.Base_Test import BaseTestHome
from Tests.Base_Test import BaseTestLogin
from Pages.Login_Page import LoginPage
import unittest
from HTMLTestRunner import HTMLTestRunner


class ChangingPageToLogin(BaseTestHome):
    def test_changing_page_to_the_user_login_page(self):
        home_page = HomePage(self.driver)
        home_page.click_header_account_button()
        title = "Logowanie - Sport-Shop.pl"
        assert self.driver.title == title


class LoginTestPositive(BaseTestLogin):
    def test_positive_login(self):
        email = "abc@gmail.com"
        password = "haslo123"
        login_page = LoginPage(self.driver)
        login_page.entering_email(email)
        login_page.entering_password(password)
        login_page.click_sign_in_button()
        assert self.driver.title == "Historia zakupów - Sport-Shop.pl"


class LoginTestNegative(BaseTestLogin):
    def test_negative_login_wrong_password(self):
        email = "abc@gmail.com"
        wrong_password = "..."
        login_page = LoginPage(self.driver)
        login_page.entering_email(email)
        login_page.entering_password(wrong_password)
        login_page.click_sign_in_button()
        expected_error = "Nieprawidłowy adres e-mail lub hasło"
        login_page.error_message(expected_error)

    def test_negative_login_no_password_entered(self):
        email = "abc@gmail.com"
        login_page = LoginPage(self.driver)
        login_page.entering_email(email)
        login_page.click_sign_in_button()
        expected_error = "Please fill out this field."
        login_page.no_password_entered_message(expected_error)


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='../test_reports'))
