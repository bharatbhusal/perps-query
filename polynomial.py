import requests

api_url = "https://perps-api-experimental.polynomial.fi/snx-perps/markets/v2"


def get_market_data():
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


def parse_data(data):
    for i, each in enumerate(data):
        print(
            f"{i+1}) pair: {each['asset']}\t Fundaing Rate: {float(each['fundingRatePercentageLast1h'])/ (10**18)}"
        )


if __name__ == "__main__":
    market_data = get_market_data()
    parse_data(market_data)
