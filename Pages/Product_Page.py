from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPageLocators:
    SIZE_SELECTION_BUTTON = (By.ID, "select_attrib")
    SIZE_SELECTION_42 = (By.XPATH, '//div[@class="size-text" and normalize-space(text())="42"]')
    SIZE_SELECTION_44 = (By.XPATH, '//div[@class="size-text" and normalize-space(text())="44"]')
    ADD_TO_SHOPPING_CART_BUTTON = (By.ID, "button_koszyk")
    CLOSE_SHOPPING_CART_BUTTON = (By.XPATH, '//button[@class="close"]')
    TO_THE_SHOPPING_CART_BUTTON = (By.XPATH, '//a[@class="btn btn-secondary"]')


class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    def click_size_selection_button(self):
        size_selection_button = self.driver.find_element(*ProductPageLocators.SIZE_SELECTION_BUTTON)
        size_selection_button.click()

    def click_size_42(self):
        size_42 = self.driver.find_element(*ProductPageLocators.SIZE_SELECTION_42)
        size_42.click()

    def click_add_to_shopping_cart_button(self):
        add_to_shopping_cart_button = self.driver.find_element(*ProductPageLocators.ADD_TO_SHOPPING_CART_BUTTON)
        add_to_shopping_cart_button.click()

    def click_close_shopping_cart_button(self):
        close_shopping_cart_button = self.driver.find_element(*ProductPageLocators.CLOSE_SHOPPING_CART_BUTTON)
        close_shopping_cart_button.click()

    def click_size_44(self):
        size_44 = self.driver.find_element(*ProductPageLocators.SIZE_SELECTION_44)
        size_44.click()

    def click_your_shopping_cart_button(self):
        shopping_cart_button = self.driver.find_element(*ProductPageLocators.TO_THE_SHOPPING_CART_BUTTON)
        shopping_cart_button.click()
