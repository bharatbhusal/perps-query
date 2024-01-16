import requests
import json

API_URL = "https://api.hyperliquid.xyz/info"
PAYLOAD = {"type": "metaAndAssetCtxs"}
HEADERS = {"Content-Type": "application/json"}


def send_request():
    try:
        response = requests.post(API_URL, data=json.dumps(PAYLOAD), headers=HEADERS)
        response.raise_for_status()
        return response
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
        raise
    except json.JSONDecodeError as err:
        print(f"JSON decoding error occurred: {err}")
        raise


def extract_tokens(data):
    return data[0]["universe"]


def extract_token_details(data):
    return data[1]


def calculate_funding_rate(token_details):
    return [round(float(each["funding"]) * 100, 4) for each in token_details]


def extract_token_names(tokens):
    return [each["name"] for each in tokens]


def handle_request_exception(exception):
    print(f"Error: {exception}")


def get_market_data():
    try:
        response = send_request()
        data = response.json()
        tokens = extract_tokens(data)
        token_details = extract_token_details(data)
        funding_rate = calculate_funding_rate(token_details)
        token_name = extract_token_names(tokens)
        details = list(zip(token_name, funding_rate))
        return details
    except requests.exceptions.RequestException as e:
        handle_request_exception(e)
        return None


def parse_data(data):
    for i, (token_name, funding_rate) in enumerate(data):
        print(f"{i+1}) Token Name: {token_name}\t Funding Rate: {funding_rate}%")


if __name__ == "__main__":
    market_data = get_market_data()

    if market_data is not None:
        parse_data(market_data)
