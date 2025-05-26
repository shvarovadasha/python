import json
import time
import requests
from bs4 import BeautifulSoup

base_url = "https://www.scrapethissite.com/pages/forms/?page="
teams = []

for page in range(1, 11):
    url = base_url + str(page)
    print(f"Парсим страницу: {url}")

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    rows = soup.select('tr.team')

    if not rows:
        print("Достигнута последняя страница или данные не найдены.")
        break

    for row in rows:
        name = row.select_one('td.name').text.strip()
        year = row.select_one('td.year').text.strip()
        wins = row.select_one('td.wins').text.strip()
        losses = row.select_one('td.losses').text.strip()

        teams.append({
            'name': name,
            'year': year,
            'wins': wins,
            'losses': losses
        })

    time.sleep(3) 

with open('teams.json', 'w', encoding='utf-8') as f:
    json.dump(teams, f, ensure_ascii=False, indent=4)

print(f"Собрано {len(teams)} команд")
