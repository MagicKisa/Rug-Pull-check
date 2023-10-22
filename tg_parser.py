import json

dx_data = None
with open("dx_data.json", 'r') as file:
    dx_data = json.load(file)

tg = dict()
tg['urls'] = []

for item in dx_data['items']:
    if item['telegramUrl']:
        tg['urls'].append(item['telegramUrl'])

with open("tg_list.json", 'w') as file:
    json.dump(tg, file)
