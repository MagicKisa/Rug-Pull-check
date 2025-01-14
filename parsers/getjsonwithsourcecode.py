import requests
import json

# Сбор кодов криптовалют по их имеющимся данным

def get_api_info(apis_dict, name):
    url = None
    apikey = None
    for api in apis_dict["apis"]:
        if api["scan_name"] == name:
            url = api["url"]
            apikey = api["apikey"]
    return (url, apikey)


def valid_info(url, apikey):
    return url is not None and apikey is not None

def data_from_json(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def get_chain_name_from_item(item):
    try:
        return item['currency_data']['data']['contracts'][0]['platform']['name']
    except:
        return False

def get_address_from_item(item):
    return item['currency_data']['data']['contracts'][0]['address']

def get_token_name_from_item(item):
    return item['currency_data']['data']['name']

def get_life_cycle_from_item(item):
    return item['lifeCycle']

data = dict()
with open("../data/currency_data.json", "r") as file:
    data = json.load(file)
apis_dict = data_from_json("apis_dict.json")


res_data = {'items':[]}

for item in data["items"]:
    name = get_chain_name_from_item(item)
    if not name:
        continue
    address = get_address_from_item(item)
    token_name = get_token_name_from_item(item)
    life_cycle = get_life_cycle_from_item(item)

    url, apikey = get_api_info(apis_dict, name)
    if valid_info(url, apikey):

        # Выполнение GET-запроса
        params = {"module": "contract", "action": "getsourcecode", "address": address, "apikey": apikey}
        response = requests.get(url, params=params)

        # Проверка успешности запроса
        if response.status_code == 200:
            res_data['items'].append({'name': token_name, 'lifeCycle': life_cycle,
                              'response': response.json()})  # Извлечение данных из JSON-ответа
        else:
            print(f"Ошибка {response.status_code}: {response.text}")

with open("../data/cryptorank_data.json", "w") as file:
    json.dump(res_data, file)