
from selenium import webdriver
from selenium.webdriver.common.by import By



driver = webdriver.Chrome('/Users/mac/Documents/WebDriver/chromedriver')
driver.get('https://www.annapurnapost.com')
driver.implicitly_wait(30)
titles = driver.find_element_by_class_name('main-title')
title = titles.text
# for title in titles:
#     print(title.text, '\n')
#     title.click
#     driver.implicitly_wait(30)

titles.click()

news = driver.find_element_by_class_name('news-content').find_elements_by_tag_name('p')
# print(type(news), '\n')
# list_news = news.find_elements_by_tag_name('p')
# print(type(list_news), '\n')
content = ''

for i in news:
    content += i.get_attribute('innerHTML')
            

print(content)



python_data = dict(title=title, content=content)

print(python_data)