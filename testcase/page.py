from selenium.common.exceptions import NoSuchElementException        

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):
    
    def has_search_button(self):
        try:
            self.driver.find_element_by_id('btn_encontre_ortopedista')
        except NoSuchElementException:
            return False
        return True