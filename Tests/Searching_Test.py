from Tests.Base_Test import BaseTestHome
from Pages.Home_Page import HomePage
from Pages.Search_Results_Page import SearchResultsPage
import unittest
from HTMLTestRunner import HTMLTestRunner


class SearchingTest(BaseTestHome):
    def test_searching_positive(self):
        product = "Buty EQ21 Run Adidas"
        home_page = HomePage(self.driver)
        home_page.entering_product_into_search_engine(product)
        home_page.click_search_button()
        search_results_page = SearchResultsPage(self.driver)
        search_results_page.checking_search_results_positive(product)

    def test_searching_negative(self):
        product = "Buty EQ22222 Run Adidas"
        home_page = HomePage(self.driver)
        home_page.entering_product_into_search_engine(product)
        home_page.click_search_button()
        expected_error = "Nie znaleziono produktów wg podanej frazy"
        search_results_page = SearchResultsPage(self.driver)
        search_results_page.checking_search_result_negative(expected_error)


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='../test_reports'))
