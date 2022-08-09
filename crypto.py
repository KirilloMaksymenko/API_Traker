import requests
import json
import config

def request_crypto_api(crypto):
    request_url = f"https://data.messari.io/api/v1/assets/{crypto}/metrics"
    data = json.loads(requests.get(request_url).content)
    price = data["data"]["market_data"]["price_usd"]
    name = data["data"]["name"]
    content = {
        "name": name,
        "price":price,
    }

    return content


