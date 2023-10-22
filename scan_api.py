import requests
import json

def get_api_info(apis_dict, ID):
    url = None
    apikey = None
    for api in apis_dict["apis"]:
        if api["chainID"] == ID:
            url = api["url"]
            apikey = api["apikey"]
    return (url, apikey)
def valid_info(url, apikey):
    return url is not None and apikey is not None

def data_from_json(filename):
    with open(filename, 'r') as file:
        return json.load(file)

dx_data = data_from_json("dx_data.json")
apis_dict = data_from_json("apis_dict.json")
scan_data = []
for item in dx_data["items"]:

    ID = item["chainID"]
    address = str(item['tokenOfSale'])

    url, apikey = get_api_info(apis_dict, ID)
    if valid_info(url, apikey):
        
        # Выполнение GET-запроса
        params = {"module": "contract", "action" : "getsourcecode", "address" : address, "apikey": apikey}
        response = requests.get(url, params=params)

        # Проверка успешности запроса
        if response.status_code == 200:
            scan_data.append(response.json())  # Извлечение данных из JSON-ответа
            print(scan_data)
        else:
            print(f"Ошибка {response.status_code}: {response.text}")

scan_json = dict()
scan_json["responses"] = scan_data

with open("scan_data.json", "w") as file:
    json.dump(scan_json, file)


