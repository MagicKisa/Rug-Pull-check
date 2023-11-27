import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import json
import time
import subprocess
import sys

platforms_url = "https://cryptorank.io/fundraising-platforms"
platforms_class = 'sc-d76e30e5-1 gyiaYN'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    # Другие заголовки по необходимости
}
def extract_links_by_class(url, params, class_):
    response = requests.get(url, params=params)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    # Анализ HTML
    links = soup.find_all('a', href=True, class_=class_)
    return links

def extract_coin_json(name_of_coin):
    time.sleep(1)
    response = requests.get(f"https://cryptorank.io/ico/{name_of_coin}")
    if response.status_code == 200:
    # Получаем HTML-код из содержимого ответа
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        # Найти тег <script> с id="__NEXT_DATA__" и type="application/json"
        next_data_script = soup.find('script', id='__NEXT_DATA__', type='application/json')
        json_data = json.loads(next_data_script.string)
        return json_data
    elif response.status_code == 429:
        time.sleep(30)
        extract_coin_json(name_of_coin)
    else:
        print(f"Ошибка при запросе: {response.status_code}")
    
    

params_list = [{"page" : 1}, {"page" : 2}]

platforms = []
for params in params_list:
    links = extract_links_by_class(platforms_url, params, class_=platforms_class)
    for link in links:
        print(link['href'])# Извлечение текста из элемента
        platforms.append(f"https://cryptorank.io{link['href']}?rows=200")


print(platforms)
data = dict()
data['items'] = []
for platform in platforms:
    keys = []
    keys_process = subprocess.run(["python", "get_coins.py", platform], capture_output=True, text=True)
    keys_output = keys_process.stdout.strip()
    try:
        keys = json.loads(keys_output)
    except json.JSONDecodeError as e:
        print(f"Ошибка при декодировании JSON: {e}")
    for key in keys:
        data['items'].append(extract_coin_json(key) )
        print(len(data['items'])) 

      
    

with open("crypto_rank1.json", "w", encoding='utf-8',newline='') as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

