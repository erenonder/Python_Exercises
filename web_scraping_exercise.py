# The modules imported in this file are located
# in the web_scraping virtual environment so
# you need to select python + virtual environment
# as build system from the build tools-build system menu
import requests
import bs4

# First exmaple to get the title of a web page
# result = requests.get("http://example.com/")

result = requests.get("https://en.wikipedia.org/wiki/Jonas_Salk")
# print(result.text) # the html source of the page
soup = bs4.BeautifulSoup(result.text, "lxml")
title_list = soup.select('title')
title = title_list[0].getText()
print(f'This is the title of your web page: {title}')

# Second Example Getting the contents section from wikipedia

# result = requests.get('https://en.wikipedia.org/wiki/Jonas_Salk')
# soup = bs4.BeautifulSoup(result.text, 'lxml')
table_of_contents = soup.select(".toctext")  # since this is a class element you use .
# first_item = soup.select(".toctext")[0]
# print(first_item.text)
# print(table_of_contents)
for index, item in enumerate(table_of_contents):
    print(f"{index:02}. {item.getText()}")

# Third Example Getting images from wikipedia

image_list = soup.select(".thumbimage")
first_image = image_list[1]
image_link = "https:" + first_image['src']
result = requests.get(image_link)
# print(result.content)
with open('Jonas_Salk.jpg', 'wb') as image_file:
    image_file.write(result.content)
