import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture")
html = r.text

soup = BeautifulSoup(html, 'html.parser')

article_body = soup.find(class_="article__chunks")

article_text = ''

for section in article_body:
    article_text += section.get_text()

print(article_text)