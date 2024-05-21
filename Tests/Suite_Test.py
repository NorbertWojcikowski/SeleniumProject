import unittest
from HTMLTestRunner import HTMLTestRunner
from Tests.Home_Page_Test import HomePageTest
from Tests.Login_Page_test import LoginTestNegative, LoginTestPositive, ChangingPageToLogin
from Tests.Registration_Test import ChangingPageToRegistration, RegistrationTestPositive, RegistrationTestNegative
from Tests.Searching_Test import SearchingTest
from Tests.Shopping_Cart_Test import ChangingPageToProductPage, CheckingOperationsOfTheShoppingCart


class TestSuite(unittest.TestSuite):
    def TestSuite(self):
        suiteTest = unittest.TestSuite()
        loader = unittest.TestLoader()
        suiteTest.addTest(HomePageTest('test_whether_the_home_page_loaded_correctly'))
        suiteTest.addTest(ChangingPageToLogin('test_changing_page_to_the_user_login_page'))
        suiteTest.addTest(LoginTestPositive('test_positive_login'))
        suiteTest.addTests(loader.loadTestsFromTestCase(LoginTestNegative))
        suiteTest.addTest(ChangingPageToRegistration('test_changing_the_page_to_the_user_registration_page'))
        suiteTest.addTest(RegistrationTestPositive('test_positive_registration'))
        suiteTest.addTests(loader.loadTestsFromTestCase(RegistrationTestNegative))
        suiteTest.addTests(loader.loadTestsFromTestCase(SearchingTest))
        suiteTest.addTest(ChangingPageToProductPage('test_changing_page_to_product_page'))
        suiteTest.addTests(loader.loadTestsFromTestCase(CheckingOperationsOfTheShoppingCart))
        return suiteTest


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='../test_reports', open_in_browser=True, title='Tests of the sport-shop.pl website', tested_by='Norbert'))
