import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":

    file_name = input(f"What would you like to name the file to which we write?   ")

    r = requests.get("https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture")
    html = r.text

    soup = BeautifulSoup(html, 'html.parser')

    article_body = soup.find(class_="article__chunks")

    article_text = ''

    for section in article_body:
        article_text += section.get_text()

    with open(f"./{file_name}.txt", 'w') as open_file:
        open_file.write(article_text)