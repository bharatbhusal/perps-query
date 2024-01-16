import requests
import json

api_url = "https://api.hyperliquid.xyz/info"


def get_market_data():
    payload = {
        "type": "metaAndAssetCtxs",
    }
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(api_url, data=json.dumps(payload), headers=headers)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes

        data = response.json()

        tokens = data[0]["universe"]
        token_details = data[1]
        funding_rate = [
            round(float(each["funding"]) * 100, 4) for each in token_details
        ]
        token_name = [each["name"] for each in tokens]
        details = list(zip(token_name, funding_rate))
        return details

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


def parse_data(data):
    for i, (token_name, funding_rate) in enumerate(data):
        print(f"{i+1}) Token Name: {token_name}\t Funding Rate: {funding_rate}%")


if __name__ == "__main__":
    market_data = get_market_data()

    if market_data is not None:
        parse_data(market_data)
