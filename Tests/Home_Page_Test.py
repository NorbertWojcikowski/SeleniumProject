from Tests.Base_Test import BaseTestHome
import unittest
from HTMLTestRunner import HTMLTestRunner


class HomePageTest(BaseTestHome):
    def test_whether_the_home_page_loaded_correctly(self):
        assert self.driver.title == "Sklep Sportowy i Turystyczny Online - Sport-Shop.pl"


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='../test_reports'))
