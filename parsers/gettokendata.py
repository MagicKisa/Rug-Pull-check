import requests
import json

# сбор данных с dxsale

# URL эндпоинта API
url = "https://scan.dx.app/api/v2/sales/offChain/successfulSales"
page = 1
# Параметры запроса, если необходимо
params = {"page": page, 'limit': 1000}

# Выполнение GET-запроса
response = requests.get(url, params=params)

# Проверка успешности запроса
if response.status_code == 200:
    data = response.json()  # Извлечение данных из JSON-ответа
else:
    print(f"Ошибка {response.status_code}: {response.text}")

totalItems = data['meta']['totalItems']
print(totalItems)
print(data['items'][1])

with open("../data/dx_data.json", "w") as file:
    json.dump(data, file)
