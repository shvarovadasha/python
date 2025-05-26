import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def selenium_parse():
    chrome_driver_path = r"C:\Users\User\.cache\selenium\chromedriver\win64\136.0.7103.113\chromedriver.exe"

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        url = 'https://news.ycombinator.com/'
        driver.get(url)

        wait = WebDriverWait(driver, 10)
        titles_elements = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tr.athing .titleline > a'))
        )

        titles_dict = {i: elem.text for i, elem in enumerate(titles_elements)}

        print("Заголовки новостей:")
        for i, title in titles_dict.items():
            print(f"{i}: {title}")

        # Сохраняем в JSON
        with open('selenium_titles.json', 'w', encoding='utf-8') as f:
            json.dump(titles_dict, f, ensure_ascii=False, indent=2)
        print("\nЗаголовки сохранены в файл selenium_titles.json")

        return titles_dict

    finally:
        driver.quit()

if __name__ == "__main__":
    selenium_parse()
