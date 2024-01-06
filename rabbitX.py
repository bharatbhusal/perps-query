import requests

api_url = "https://api.prod.rabbitx.io/markets"


def get_market_data():
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes

        data = response.json()
        return data["result"]

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


def parse_data(data):
    for i, each in enumerate(data):
        print(
            f"{i+1}) pair: {each['id']}\t Fundain Rate: {each['instant_funding_rate']}"
        )


if __name__ == "__main__":
    market_data = get_market_data()
    parse_data(market_data)
