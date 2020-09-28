import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.nytimes.com/')
html = r.text


soup = BeautifulSoup(html, 'html.parser')

headers = list(soup.find_all(['h1', 'h2', 'h3', 'h4']))
for element in headers:
    print(element.text)
