from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def close_cookies_popup(self):
    ACCEPT_COOKIES_BUTTON = (By.ID, 'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll')
    cookies_popup = WebDriverWait(self.driver, 20).until(
        EC.presence_of_element_located(ACCEPT_COOKIES_BUTTON))
    if cookies_popup.is_enabled():
        cookies_popup.click()


class BaseTestHome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.sport-shop.pl")
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        close_cookies_popup(self)

    def tearDown(self):
        self.driver.quit()


class BaseTestRegister(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.sport-shop.pl/create_account.php")
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        close_cookies_popup(self)

    def tearDown(self):
        self.driver.quit()


class BaseTestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.sport-shop.pl/login.php")
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        close_cookies_popup(self)

    def tearDown(self):
        self.driver.quit()


class BaseTestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.sport-shop.pl/buty-eq21-run-adidas-czarny-p-113368.html")
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        close_cookies_popup(self)

    def tearDown(self):
        self.driver.quit()
