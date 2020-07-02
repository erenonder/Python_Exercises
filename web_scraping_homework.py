import requests
import bs4

page_number = 1
web_page = f"http://quotes.toscrape.com/page/{page_number}/"
response = requests.get(web_page)
soup = bs4.BeautifulSoup(response.text, "lxml")

author_set = set()
quote_list = list()
tag_list = []

quotes = soup.select(".text")
for quote in quotes:
    quote_list.append(quote.getText())
    # print(quote.text)

top_ten_tags = soup.select(".tag-item")

for index, tag in enumerate(top_ten_tags):
    # print(f"{index+1}. tag {tag.text}")
    tag_list.append(tag.text)

authors = soup.select(".author")
while authors:
    # print(authors)
    for author in authors:
        author_set.add(author.text)
    # print(f"In page {page_number} author count {len(author_set)} authors {author_set}")
    page_number += 1
    web_page = f"http://quotes.toscrape.com/page/{page_number}/"
    response = requests.get(web_page)
    soup = bs4.BeautifulSoup(response.text, "lxml")
    if page_number > 50:  # something fishy going on so break the loop
        break
    authors = soup.select(".author")

for index, author in enumerate(author_set):
    print(f"{index+1:02} {author}")
