
from json import dumps
from platform import python_branch
from selenium import webdriver

driver = webdriver.Chrome('/Users/mac/Documents/WebDriver/chromedriver')

urls = 'https://www.annapurnapost.com'
news_title = []
links = []
def get_links():
    driver.get('https://www.annapurnapost.com')
    driver.implicitly_wait(30)
    titles = driver.find_elements_by_class_name('main-title')
    for title in titles:
        news_title.append(title.text)
        link = title.find_element_by_tag_name('a').get_attribute('href')
        links.append(link)
    
content = []
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


get_links()
get_content()


# print(links)
print('\n')

# print(content)

python_title_data = {"title" + str(i+1): news_title[i] for i in range(len(news_title))}

python_conent_data = {"content" + str(i+1): content[i] for i in range(len(content))}

# print(python_title_data)
# print('\n')
# print(python_conent_data)

title_json = dumps(python_title_data)

content_json = dumps(python_conent_data)

driver.close()
driver.__exit__()