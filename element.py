from selenium.common.exceptions import NoSuchElementException        

class BaseElement(object):
    def __init__(self, driver, file, page, writer):
        self.driver = driver
        self.file = file
        self.page = page
        self.writer = writer

class MainElement(BaseElement):
   def search_orthopedists(self):
    self.driver.find_element_by_id('btn_encontre_ortopedista').click()

    while(self.page.check_exists_next_page() or self.page.is_last_page()):
        orthopedists = self.driver.find_elements_by_css_selector('div.fusion-column-wrapper.encontre-ortopedista-container')

        for orthopedist in orthopedists:
            photo = orthopedist.find_element_by_class_name("encontre-ortopedista-foto").value_of_css_property("background-image").split('"')[1]
            name = orthopedist.find_element_by_class_name("encontre-ortopedista-nome").text
            specialty = orthopedist.find_element_by_class_name("encontre-ortopedista-especialidade").text
            agreement = orthopedist.find_element_by_class_name("encontre-ortopedista-crm").text
            location = orthopedist.find_element_by_class_name("encontre-ortopedista-endereco").text
            self.writer.writerow([photo, name, specialty, agreement, location])

        if(self.page.check_exists_next_page()): self.driver.find_element_by_css_selector('a.pagination-next.next').click()
    self.file.close()