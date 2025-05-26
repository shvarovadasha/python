import requests
from bs4 import BeautifulSoup

url = "https://seance.ru/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

headers = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
print("Заголовки на странице:")
for header in headers:
    print(header.text.strip())

links = soup.find_all('a', href=True)
print("\nСсылки на странице:")
for link in links:
    print(f"{link.text.strip()}: {link['href']}")
