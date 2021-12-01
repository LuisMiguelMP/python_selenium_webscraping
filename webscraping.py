# -*- encoding: utf-8 -*-
import csv
import page
import element
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
    
url = "https://sbot.org.br/localize-o-ortopedista/"

option = Options()
option.headless = False
driver = webdriver.Chrome("C:/chromedriver.exe", options=option)

driver.implicitly_wait(30)

f = open('orthopedists.csv', 'w', encoding='UTF8', newline='')
writer = csv.writer(f, delimiter=';')
header = ['photo', 'name', 'specialty', 'agreement', 'location']
writer.writerow(header)

driver.get(url)

driver.maximize_window()

mainPage = page.MainPage(driver)

element = element.MainElement(driver, f, mainPage, writer)

element.search_orthopedists()

driver.quit()