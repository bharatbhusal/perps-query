import requests
from datetime import datetime


def get_current_time_in_milliseconds():
    return int(datetime.now().timestamp() * 1000)


ONE_HOUR_IN_MILISECONDS = 60 * 60 * 1000
TO_TIME = get_current_time_in_milliseconds()
FROM_TIME = 0
TOKEN_MARKET_INDEX = 0
print(TO_TIME)
print(FROM_TIME)
SOME_API = f"https://mainnet-beta.api.drift.trade/fundingRates?marketIndex={TOKEN_MARKET_INDEX}&from={FROM_TIME}&to={TO_TIME}"
print(SOME_API)
try:
    response = requests.get(SOME_API)
    response.raise_for_status()
    print(response.json())
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
