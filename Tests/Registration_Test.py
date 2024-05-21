from Pages.Home_Page import HomePage
from Tests.Base_Test import BaseTestHome
from Tests.Base_Test import BaseTestRegister
from Pages.Login_Page import LoginPage
from Pages.Registration_Page import RegistrationPage
from ddt import data, unpack, ddt
import Test_Data.registration_data
import unittest
from HTMLTestRunner import HTMLTestRunner


class ChangingPageToRegistration(BaseTestHome):
    def test_changing_the_page_to_the_user_registration_page(self):
        home_page = HomePage(self.driver)
        home_page.click_header_account_button()
        login_page = LoginPage(self.driver)
        login_page.click_registration_account_button()
        registration_page = RegistrationPage(self.driver)
        title = "Zakładanie konta"
        registration_page.whether_registration_page_load_correctly(title)
        assert self.driver.title == "Załóż Konto - Sport-Shop.pl"


class RegistrationTestPositive(BaseTestRegister):
    def test_positive_registration(self):
        name = "Jan"
        last_name = "Kowalski"
        email = "abcde@gmail.com"
        password = "mojehaslo123"
        registration_page = RegistrationPage(self.driver)
        registration_page.entering_name(name)
        registration_page.entering_last_name(last_name)
        registration_page.entering_email(email)
        registration_page.entering_password(password)
        registration_page.entering_repeat_password(password)
        registration_page.mark_acceptance_of_the_regulations()
        registration_page.click_create_customer_account()
        assert self.driver.title == "Historia zakupów - Sport-Shop.pl"


@ddt
class RegistrationTestNegative(BaseTestRegister):
    @data(*Test_Data.registration_data.get_csv_data("../Test_Data/registration_data_negative.csv"))
    @unpack
    def test_negative_registration_no_name_entered(self, name, lastname, email, password, repeat_password):
        registration_page = RegistrationPage(self.driver)
        registration_page.entering_last_name(lastname)
        registration_page.entering_email(email)
        registration_page.entering_password(password)
        registration_page.entering_repeat_password(repeat_password)
        registration_page.mark_acceptance_of_the_regulations()
        registration_page.click_create_customer_account()
        expected_error = "To pole jest wymagane"
        registration_page.error_message(expected_error)

    @data(*Test_Data.registration_data.get_csv_data("../Test_Data/registration_data_negative.csv"))
    @unpack
    def test_negative_registration_wrong_email(self, name, lastname, email, password, repeat_password):
        registration_page = RegistrationPage(self.driver)
        registration_page.entering_name(name)
        registration_page.entering_last_name(lastname)
        registration_page.entering_email(email)
        registration_page.entering_password(password)
        registration_page.entering_repeat_password(repeat_password)
        registration_page.mark_acceptance_of_the_regulations()
        registration_page.click_create_customer_account()
        expected_error = "Wprowadzono niepoprawny adres e-mail"
        registration_page.error_message(expected_error)


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='../test_reports'))
