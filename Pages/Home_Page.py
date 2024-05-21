from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class HomePageLocators:
    HEADER_ACCOUNT_BUTTON = (By.ID, 'header-account')
    SEARCH_ENGINE_INPUT = (By.ID, "autocomplete-search-term")
    SEARCH_BUTTON = (By.XPATH, '//button[@class="submit"]')


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def click_header_account_button(self):
        action = ActionChains(self.driver)
        your_account_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(HomePageLocators.HEADER_ACCOUNT_BUTTON))
        action.move_to_element(your_account_button).click().perform()

    def entering_product_into_search_engine(self, product):
        search_input = self.driver.find_element(*HomePageLocators.SEARCH_ENGINE_INPUT)
        search_input.send_keys(product)

    def click_search_button(self):
        search_button = self.driver.find_element(*HomePageLocators.SEARCH_BUTTON)
        search_button.click()
