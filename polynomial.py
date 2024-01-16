import requests

API_URL = "https://perps-api-experimental.polynomial.fi/snx-perps/markets/v2"


def send_request():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


def parse_data(data):
    for i, market in enumerate(data):
        asset = market["asset"]
        funding_rate = float(market["fundingRatePercentageLast1h"]) / (10**18)
        print(f"{i+1}) Pair: {asset}\t Funding Rate: {round(float(funding_rate), 4)}%")


if __name__ == "__main__":
    market_data = send_request()

    if market_data is not None:
        parse_data(market_data)
