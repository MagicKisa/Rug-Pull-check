import requests
import json

def get_api_info(apis_dict, name_of_scan):
    url = None
    apikey = None
    for api in apis_dict["apis"]:
        if api["scan_name"] == name_of_scan:
            url = api["url"]
            apikey = api["apikey"]
    return (url, apikey)
def valid_info(url, apikey):
    return url is not None and apikey is not None

def data_from_json(filename):
    with open(filename, 'r') as file:
        return json.load(file)

dx_data = data_from_json("crypto_rank.json")
apis_dict = data_from_json("apis_dict.json")
scan_data = dict()
for platform in dx_data["items"]:
    for coin_name in platform['props']['pageProps']['fallbackCoins']:
        coin = platform['props']['pageProps']['fallbackCoins'][coin_name]
        scan_data[coin_name] = []
        for token in coin['tokens']:
            name_of_scan = token['platformName']
            url, apikey = get_api_info(apis_dict, name_of_scan)
            if valid_info(url, apikey):
                try:
                    address = token['address']
                except KeyError:
                    continue
                # Выполнение GET-запроса
                params = {"module": "contract", "action" : "getsourcecode", "address" : address, "apikey": apikey}
                response = requests.get(url, params=params)

                # Проверка успешности запроса
                if response.status_code == 200:
                    if len(scan_data[coin_name]) == 0:
                        scan_data[coin_name].append(response.json())  # Извлечение данных из JSON-ответа
                    print(len(scan_data[coin_name]), coin_name)
                else:
                    print(f"Ошибка {response.status_code}: {response.text}")
            else:
                print("не нашел")
                continue
            if len(scan_data[coin_name]) == 0:
                del scan_data[coin_name]


with open("contract_data.json", "w") as file:
    json.dump(scan_data, file)
