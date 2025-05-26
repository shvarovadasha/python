import csv
import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

news_items = soup.find_all('tr', class_='athing')

with open('news_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Link', 'Comments'])

    for item in news_items:
        title_tag = item.find('span', class_='titleline')
        if not title_tag:
            continue

        title_link = title_tag.find('a')
        if not title_link:
            continue

        title = title_link.text
        link = title_link['href']

        next_tr = item.find_next_sibling('tr')
        comment_tag = next_tr.find_all('a')[-1]

        comments_text = comment_tag.text if 'comment' in comment_tag.text else '0 comments'

        writer.writerow([title, link, comments_text])

print("Данные успешно сохранены в файл news_data.csv")
