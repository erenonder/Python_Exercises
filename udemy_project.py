import requests
import bs4

page = 1
website = f"http://books.toscrape.com/catalogue/page-{page}.html"

response = requests.get(website)

while response:
    soup = bs4.BeautifulSoup(response.text, "lxml")
    all_books = soup.select('.product_pod')

    for index, book in enumerate(all_books):
        if book.select('.star-rating.Two'):
            print(f"page: {page:02} name: {book.select('a')[1]['title']}")

    page += 1
    website = f"http://books.toscrape.com/catalogue/page-{page}.html"
    response = requests.get(website)

