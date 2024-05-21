from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchResultsPageLocators:
    PRODUCT_LISTING = (By.XPATH, '//div[@class="listings"]/div')
    PRODUCT_NOT_FOUND = (By.XPATH, '//div[@id="search_no_result"]/h3')
    CLICK_SPECIFIC_PRODUCT = (By.XPATH, '(//a[@title="Buty EQ21 Run Adidas"])[1]')


class SearchResultsPage:
    def __init__(self, driver):
        self.driver = driver

    def checking_search_results_positive(self, product):
        results = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(SearchResultsPageLocators.PRODUCT_LISTING))
        all_results_match = True
        for result in results:
            product_name = result.text
            if product.lower() not in product_name.lower():
                all_results_match = False
                print(f"Product name mismatch: {product_name}")
                break
        if all_results_match:
            print("All product names match the search query.")
        else:
            print("Some product names do not match the search query.")

    def checking_search_result_negative(self, expected_error):
        error = self.driver.find_element(*SearchResultsPageLocators.PRODUCT_NOT_FOUND)
        assert error.text == expected_error

    def click_specific_product(self):
        specific_product = self.driver.find_element(*SearchResultsPageLocators.CLICK_SPECIFIC_PRODUCT)
        specific_product.click()

