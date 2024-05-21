from Tests.Base_Test import BaseTestHome
from Pages.Home_Page import HomePage
from Pages.Search_Results_Page import SearchResultsPage
from Tests.Base_Test import BaseTestShoppingCart
from Pages.Product_Page import ProductPage
from Pages.Shopping_Cart_Page import ShoppingCartPage
import unittest
from HTMLTestRunner import HTMLTestRunner


class ChangingPageToProductPage(BaseTestHome):
    def test_changing_page_to_product_page(self):
        product = "Buty EQ21 Run Adidas"
        home_page = HomePage(self.driver)
        home_page.entering_product_into_search_engine(product)
        home_page.click_search_button()
        search_results_page = SearchResultsPage(self.driver)
        search_results_page.click_specific_product()
        page_title = "Buty EQ21 Run Adidas - czarny - Kup w Sport-Shop!"
        assert self.driver.title == page_title


class CheckingOperationsOfTheShoppingCart(BaseTestShoppingCart):
    def test_checking_the_total_price_in_the_shopping_cart(self):
        product_page = ProductPage(self.driver)
        product_page.click_size_selection_button()
        product_page.click_size_42()
        product_page.click_add_to_shopping_cart_button()
        product_page.click_close_shopping_cart_button()
        product_page.click_size_selection_button()
        product_page.click_size_44()
        product_page.click_add_to_shopping_cart_button()
        product_page.click_your_shopping_cart_button()
        shopping_cart_page = ShoppingCartPage(self.driver)
        shopping_cart_page.sum_validation()

    def test_checking_the_value_of_delivery_should_be_non_zero(self):
        product_page = ProductPage(self.driver)
        product_page.click_size_selection_button()
        product_page.click_size_42()
        product_page.click_add_to_shopping_cart_button()
        product_page.click_your_shopping_cart_button()
        expected_delivery_value = "9,99 zł"
        shopping_cart_page = ShoppingCartPage(self.driver)
        shopping_cart_page.the_value_of_delivery_validation(expected_delivery_value)

    def test_checking_the_value_of_delivery_should_be_zero(self):
        product_page = ProductPage(self.driver)
        product_page.click_size_selection_button()
        product_page.click_size_42()
        product_page.click_add_to_shopping_cart_button()
        product_page.click_close_shopping_cart_button()
        product_page.click_size_selection_button()
        product_page.click_size_44()
        product_page.click_add_to_shopping_cart_button()
        product_page.click_your_shopping_cart_button()
        expected_delivery_value = "0,00 zł"
        shopping_cart_page = ShoppingCartPage(self.driver)
        shopping_cart_page.the_value_of_delivery_validation(expected_delivery_value)

    def test_remove_product_from_the_basket(self):
        product_page = ProductPage(self.driver)
        product_page.click_size_selection_button()
        product_page.click_size_42()
        product_page.click_add_to_shopping_cart_button()
        product_page.click_your_shopping_cart_button()
        shopping_cart_page = ShoppingCartPage(self.driver)
        shopping_cart_page.click_remove_from_basket_button()
        expected_message = "Twój koszyk jest pusty!"
        shopping_cart_page.empty_basket_message(expected_message)


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='../test_reports'))
