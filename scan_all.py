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
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

dx_data = data_from_json("crypto_rank1.json")
apis_dict = data_from_json("apis_dict.json")
scan_data = dict()
print(dx_data['items'][0]['props']['pageProps']['coin'])
need_platforms = dict()
for coin in dx_data["items"]:
    try:
        coin_info = coin['props']['pageProps']['coin']
    except TypeError:
        continue
    coin_name = coin_info['name']
    for token in reversed(coin_info['tokens']):
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
                scan_data[coin_name] = response.json()  # Извлечение данных из JSON-ответа
                print(len(scan_data), coin_name)
                break
            else:
                print(f"Ошибка {response.status_code}: {response.text}")
        else:
            print("не нашел")
        if coin_name not in scan_data:
            if token['platformName'] not in need_platforms:
                need_platforms[token['platformName']] = 1
            else:
                need_platforms[token['platformName']] += 1
            

with open("contract_data.json", "w") as file:
    json.dump(scan_data, file)

print(need_platforms)
