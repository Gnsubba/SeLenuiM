from json import dumps
from selenium import webdriver
from selenium.webdriver.common.by import By

# Making the object of webdiver and using the Chrome driver and giving the path to the downloaded chromedriver.
driver = webdriver.Chrome('/Users/mac/Documents/WebDriver/chromedriver')

# Function to click the search button and give the parameter and click event
def search():
    driver.get('https://www.annapurnapost.com')

    search_button = driver.find_element_by_id('global-search-trigger')
    print(type(search_button))
    search_button.click()

    search_button1 = driver.find_element_by_id('searchField')

    search_button1.send_keys('सरकार')

    search_button2 = driver.find_element_by_class_name('btn-search')
    search_button2.click()

   
    

search()

# List for storing the titles 
news_title = []

# List for storing extracted links
links = []

# Storing the current url of the redirected page after searching
searched_url = driver.current_url

# Reinitializing of the driver
driver.get(searched_url)

# Waiting for the page to be loaded
driver.implicitly_wait(30)

# Searching the element in the page by class_name which returns list
element = driver.find_elements_by_class_name('media-right')
for tags in element:
    news_title.append(tags.text)
    tag = tags.find_element_by_tag_name('a')
    link = tag.get_attribute('href')
    links.append(link)
    # print(link)


# tag = element.find_element_by_tag_name('a')
# link = tag.get_attribute('href')
# print(link)

# content list to store the content
content = []

# Function to get the content from the extracted links or urls
def get_content():
    for link in links:
        driver.get(str(link))
        para_element = driver.find_elements_by_class_name('news-content')
        for para in para_element:
            senten = para.find_element_by_tag_name('p')
            sentens = senten.get_attribute('innerHTML')
            content.append(sentens)
            print(sentens)
            print('\n')
            print('\n')
            print('\n')


get_content()

# Storing the list of title and content in dictionay format respectively.
python_title_data = {"title" + str(i+1): news_title[i] for i in range(len(news_title))}
python_conent_data = {"content" + str(i+1): content[i] for i in range(len(content))}



# converting python dictionary to json format
title_json = dumps(python_title_data)
content_json = dumps(python_conent_data)


# Closing the browser after compeleting the task
driver.close()
driver.__exit__()