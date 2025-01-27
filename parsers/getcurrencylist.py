import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import json
import time
import subprocess
import sys

# Собрать список всех криптовалют

f = open('x-api-key', 'r')
xapikey = f.read()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'X-api-key': xapikey
    # Другие заголовки по необходимости
}

def extract_crypto_currency_list():
    params = {
        'include': 'lifeCycle'
    }

    response = requests.get(f"https://api.cryptorank.io/v2/currencies/map", params=params, headers=headers)
    if response.status_code == 200:
    # Получаем HTML-код из содержимого ответа
        data = response.json()
        print(data)
        return data

    else:
        print(f"Ошибка при запросе: {response.status_code}")

data = extract_crypto_currency_list()

with open("../data/crypto_list.json", "w") as file:
    json.dump(data, file)



