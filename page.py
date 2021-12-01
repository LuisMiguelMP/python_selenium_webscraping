from selenium.common.exceptions import NoSuchElementException        

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):
    def check_exists_next_page(self):
        try:
            self.driver.find_elements_by_css_selector('a.pagination-next.next')
        except NoSuchElementException:
            return False
        return True

    def check_exists_previous_page(self):
        try:
            self.driver.find_elements_by_css_selector('a.pagination-prev.prev')
        except NoSuchElementException:
            return False
        return True

    def is_last_page(self):
        return (self.check_exists_previous_page() and not(self.check_exists_next_page()) or (not(self.check_exists_previous_page()) and not(self.check_exists_next_page())))