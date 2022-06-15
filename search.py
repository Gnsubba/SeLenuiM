from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('/Users/mac/Documents/WebDriver/chromedriver')

driver.get('https://www.annapurnapost.com')

search_button = driver.find_element_by_id('global-search-trigger')
print(type(search_button))
search_button.click()

search_button1 = driver.find_element_by_id('searchField')

search_button1.send_keys('सरकार')

search_button2 = driver.find_element_by_class_name('btn-search')
search_button2.click()
