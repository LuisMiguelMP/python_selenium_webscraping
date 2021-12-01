import page
import unittest
from selenium import webdriver

class SbotOrgBrSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:/chromedriver.exe")
        self.driver.get("https://sbot.org.br/localize-o-ortopedista/")

    def test_page(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.has_search_button()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()