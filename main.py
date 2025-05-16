import requests
from bs4 import BeautifulSoup
import csv
import json

url = 'http://books.toscrape.com/catalogue/page-1.html'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

books = []

for book in soup.select('article.product_pod'):
    title = book.h3.a['title']
    price = book.select_one('.price_color').text.strip()
    availability = book.select_one('.availability').text.strip()
    rating = book.p['class'][1]  # misalnya 'One', 'Two', ...
    link = "http://books.toscrape.com/catalogue/" + book.h3.a['href']
    
    books.append({
        'title': title,
        'price': price,
        'availability': availability,
        'rating': rating,
        'link': link
    })

# Simpan ke JSON
with open('books.json', 'w', encoding='utf-8') as f:
    json.dump(books, f, ensure_ascii=False, indent=2)

# Simpan ke CSV
with open('books.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['title', 'price', 'availability', 'rating', 'link'])
    writer.writeheader()
    writer.writerows(books)
