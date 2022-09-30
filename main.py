import requests
from bs4 import BeautifulSoup


HEADERS = {
    'Host': 'habr.com',
    'Accept Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,sv;q=0.6,zh-CN;q=0.5,zh;q=0.4,ko;q=0.3',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Cache-Control': 'max-age=0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0'
    'Safari/537.36',
    'sec-ch-ua-mobile': '?0'
}

KEYWORDS = {'дизайн', 'фото', 'web', 'python'}



response = requests.get('https://habr.com/ru/all/', headers=HEADERS)
text = response.text
soup = BeautifulSoup(text, features='html.parser')
articles = soup.find_all(class_='tm-articles-list__item')

for article in articles:
    href = set(article.get_text('' , strip=True).lower().split())
    if KEYWORDS & href:
        link = "https://habr.com" + article.find('h2').find('a').attrs.get('href')
        title = article.find('h2').find('a').find('span').text
        data = article.find('time').attrs.get('title')
        print(f'{data} - {title} - {link}')