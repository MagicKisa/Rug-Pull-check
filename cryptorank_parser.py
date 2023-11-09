import requests
from bs4 import BeautifulSoup 
import json
import time
# Загрузка страницы

platforms_url = "https://cryptorank.io/fundraising-platforms"
platforms_class = 'sc-d76e30e5-1 gyiaYN'

def extract_links_by_class(url, params, class_):
    response = requests.get(url, params=params)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    # Анализ HTML
    links = soup.find_all('a', href=True, class_=class_)
    return links
params_list = [{"page" : 1}, {"page" : 2}]

platforms = []
for params in params_list:
    links = extract_links_by_class(platforms_url, params, class_=platforms_class)
    for link in links:
        print(link['href'])# Извлечение текста из элемента
        platforms.append(f"https://cryptorank.io{link['href']}")

print(platforms)
data = dict()
data['items'] = []
for platform in platforms:
    url = platform
    response = requests.get(url, params={"rows": 200, "page": 3})
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        # Найти тег <script> с id="__NEXT_DATA__" и type="application/json"
        next_data_script = soup.find('script', id='__NEXT_DATA__', type='application/json')

        if next_data_script:
            # Извлечь JSON-данные из содержимого тега
            json_data = json.loads(next_data_script.string)
        data['items'].append(json_data)  # Добавить данные текущей страницы к общим данным
        print(len(json_data['props']['pageProps']['fallbackCoins'].keys()))
    elif response.status_code == 429:
        time.sleep(30)
        print('wait..')
    else:
        print(f"Ошибка запроса{page} {response.status_code}")


with open("crypto_rank2.json", "w", encoding='utf-8',newline='') as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

for i in range(len(data['items'])):
    print(data['items'][i]['props']['pageProps']['fallbackCoins'].keys())
