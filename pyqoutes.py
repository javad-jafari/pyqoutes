"""
This project get request to quotes.toscrape.com and scrap data.
get these data :quotes, authors, tags

"""

import requests
from bs4 import BeautifulSoup




def find_quotes(page_no):
    url = f"https://quotes.toscrape.com/page/{page_no}"
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'lxml') 
    quotes = soup.find_all('span', class_='text')
    authors = soup.find_all('small', class_='author')
    tags = soup.find_all('div', class_='tags')
    for i in range(0, len(quotes)):
        print(50*'*')
        print(quotes[i].text)
        print(authors[i].text)
        quotes_tags = tags[i].find_all('a', class_='tag')
        for tag in quotes_tags:
            if tag == quotes_tags[-1]:
                print(tag.text, end="\n")
            else:
                print(tag.text, end="-")
        print(50*'*','\n')
        print()


