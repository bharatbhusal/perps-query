import requests

API_URL = "https://api.prod.rabbitx.io/markets"


def send_request():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        return response.json()["result"]
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


def parse_data(data):
    for i, market in enumerate(data):
        pair_id = market["id"]
        funding_rate = market["last_funding_rate_basis"]
        print(
            f"{i+1}) Pair: {pair_id}\t Funding Rate: {round(float(funding_rate)*100, 4)}%"
        )


if __name__ == "__main__":
    market_data = send_request()

    if market_data is not None:
        parse_data(market_data)
