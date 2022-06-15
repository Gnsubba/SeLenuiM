
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('/Users/mac/Documents/WebDriver/chromedriver')
driver.get('https://www.annapurnapost.com')
driver.implicitly_wait(30)
titles = driver.find_element_by_class_name('main-title')
# for title in titles:
#     print(title.text, '\n')
#     title.click
#     driver.implicitly_wait(30)

titles.click()

news = driver.find_element_by_class_name('news-content').find_elements_by_tag_name('p')
# print(type(news), '\n')
# list_news = news.find_elements_by_tag_name('p')
# print(type(list_news), '\n')
for i in news:
    try:
        i.find_element_by_class_name('ad-inside-news')
        continue
    except:
        try:
            i.find_element_by_tag_name('a')
            continue
        except:
            print(i.get_attribute('innerHTML'))
            
    



