import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import json
import time
import subprocess
import sys

# собрать данные (id, name, contract_addresses) имея список криптовалют

f = open('x-api-key', 'r')
xapikey = f.read()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'X-api-key': xapikey
    # Другие заголовки по необходимости
}

def extract_crypto_currency_data(currence_id):

    response = requests.get(f"https://api.cryptorank.io/v2/currencies/{currence_id}", headers=headers)
    if response.status_code == 200:
    # Получаем HTML-код из содержимого ответа
        data = response.json()
        print(data)
        return data
    else:
        print(f"Ошибка при запросе: {response.status_code}")
        time.sleep(5)

data = dict()
with open("../data/crypto_list.json", "r") as file:
    data = json.load(file)


with open("../data/currency_data.json", "r") as file:
    currency_data_dict = json.load(file)

start_i = 1199
end_i = 1599

currency_data = currency_data_dict['items']
for i in range(start_i, end_i):
    item = data['data'][i]
    time.sleep(1)
    currency_data.append({'lifeCycle': item['lifeCycle'], 'currency_data': extract_crypto_currency_data(item['id'])})
    print(len(currency_data))

currency_data_dict = {'items' : currency_data}
with open("../data/currency_data.json", "w") as file:
    json.dump(currency_data_dict, file)