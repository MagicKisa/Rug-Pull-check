import json
import os


def create_apis_dict():
    bnb_key = os.environ.get('bnb_key')
    fantom_key = os.environ.get('fantom_key')
    core_key = os.environ.get('core_key')
    arbitrum_key = os.environ.get('arbitrum_key')
    base_key = os.environ.get('base_key')
    polygon_key = os.environ.get('polygon_key')
    ethereum_key = os.environ.get('ethereum_key')


    apis_dict = {"apis": [{"scan_name": "Fantom", "apikey": fantom_key, "url": "https://api.ftmscan.com/api", "chainID": 250},
                          {"scan_name": "BNB", "apikey": bnb_key, "url": "https://api.bscscan.com/api", "chainID": 56},
                          {"scan_name": "Core", "apikey": core_key, "url": "https://openapi.coredao.org/api", "chainID": 1116},
                          {"scan_name": "Arbitrum", "apikey": arbitrum_key, "url": "https://api.arbiscan.io/api", "chainID": 42161},
                          {"scan_name": "Base", "apikey": base_key, "url": "https://api.basescan.org/api", "chainID": 8453},
                          {"scan_name": "Polygon", "apikey": polygon_key, "url": "https://api.polygonscan.com/api", "chainID": 137},
                          {"scan_name": "Ethereum", "apikey": ethereum_key, "url": "https://api.etherscan.io/api", "chainID": 1}]}

    with open('apis_dict.json', 'w') as f:
        json.dump(apis_dict, f)