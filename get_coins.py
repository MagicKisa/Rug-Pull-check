# get_coins.py
import json
import re
import time
import sys
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)
driver.get(sys.argv[1])

keys_found = False
keys = None

try:
    # Ждем, пока не появится запрос к API
    while not keys_found:
        entries = driver.execute_script("return window.performance.getEntries();")

        for entry in entries:
            if "api.cryptorank.io/v0/coins/prices?" in entry.get("name", ""):
                request_url = entry.get("name")
                match = re.search(r'prices\?keys=(.*)', request_url)
                if match:
                    keys = match.group(1).split(',')
                    keys[-1] = keys[-1].split('&')[0]
                    keys_found = True

        time.sleep(1)

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    driver.quit()

# Выводим ключи в формате JSON
if keys is not None:
    print(json.dumps(keys))
else:
    print("Ключи не найдены")



