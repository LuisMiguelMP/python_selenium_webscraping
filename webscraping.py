# -*- encoding: utf-8 -*-
import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException        


def check_exists_next_page():
    try:
        driver.find_elements_by_css_selector('a.pagination-next.next')
    except NoSuchElementException:
        return False
    return True

def check_exists_previous_page():
    try:
        driver.find_elements_by_css_selector('a.pagination-prev.prev')
    except NoSuchElementException:
        return False
    return True

def is_last_page():
    return (check_exists_previous_page() and not(check_exists_next_page()))

def search_orthopedists():
    driver.find_element_by_id('btn_encontre_ortopedista').click()

    while(check_exists_next_page() or is_last_page()):
        orthopedists = driver.find_elements_by_css_selector('div.fusion-column-wrapper.encontre-ortopedista-container')

        for orthopedist in orthopedists:
            photo = orthopedist.find_element_by_class_name("encontre-ortopedista-foto").value_of_css_property("background-image").split('"')[1]
            name = orthopedist.find_element_by_class_name("encontre-ortopedista-nome").text
            specialty = orthopedist.find_element_by_class_name("encontre-ortopedista-especialidade").text
            agreement = orthopedist.find_element_by_class_name("encontre-ortopedista-crm").text
            location = orthopedist.find_element_by_class_name("encontre-ortopedista-endereco").text
            writer.writerow([photo, name, specialty, agreement, location])

        if(check_exists_next_page()): driver.find_element_by_css_selector('a.pagination-next.next').click()
    f.close()
    
url = "https://sbot.org.br/localize-o-ortopedista/"

option = Options()
option.headless = False
driver = webdriver.Chrome(options=option)

driver.implicitly_wait(30)

f = open('orthopedists.csv', 'w', encoding='UTF8', newline='')
writer = csv.writer(f, delimiter=';')
header = ['photo', 'name', 'specialty', 'agreement', 'location']
writer.writerow(header)

driver.get(url)

search_orthopedists()

driver.quit()