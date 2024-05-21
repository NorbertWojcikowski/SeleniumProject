from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShoppingCartPageLocators:
    PRICES_OF_PRODUCTS = (By.XPATH, '//div[@class="suma"]')
    TOTAL_AMOUNT = (By.XPATH, '//div[@class="total"]/span')
    DELIVERY_VALUE = (By.XPATH, '//div[@class="dostawa_koszty"]/div[2]/b')
    REMOVE_FROM_BASKET_BUTTON = (By.XPATH, '//a[@class="remove_from_basket"]')
    EMPTY_BASKET_TEXT = (By.XPATH, '//div[@class="empty"]')


class ShoppingCartPage:
    def __init__(self, driver):
        self.driver = driver

    def sum_validation(self):
        prices = self.driver.find_elements(*ShoppingCartPageLocators.PRICES_OF_PRODUCTS)
        amount = 0
        for price in prices[1:]:
            price_text = price.text
            cleaned_price_text = price_text.replace('zł', '').replace('\n', '').replace(',', '.').replace('379.00', '').strip()
            amount = amount + float(cleaned_price_text)
        total_amount = self.driver.find_element(*ShoppingCartPageLocators.TOTAL_AMOUNT).text
        cleaned_total_amount = float(total_amount.replace('zł', '').replace('\n', '').replace(',', '.').strip())
        assert amount == cleaned_total_amount

    def the_value_of_delivery_validation(self, expected_delivery_value):
        delivery_value = self.driver.find_element(*ShoppingCartPageLocators.DELIVERY_VALUE)
        assert delivery_value.text == expected_delivery_value

    def click_remove_from_basket_button(self):
        remove_from_basket_button = self.driver.find_element(*ShoppingCartPageLocators.REMOVE_FROM_BASKET_BUTTON)
        remove_from_basket_button.click()

    def empty_basket_message(self, expected_message):
        message = self.driver.find_element(*ShoppingCartPageLocators.EMPTY_BASKET_TEXT)
        assert (expected_message in message.text)

