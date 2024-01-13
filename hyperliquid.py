import requests
import json
import time
from datetime import datetime, timedelta


class TimeConverter:
    def __init__(self):
        pass

    @staticmethod
    def milliseconds_to_localtime(milliseconds):
        seconds = milliseconds / 1000
        utc_time = datetime.utcfromtimestamp(seconds)
        local_time = utc_time.replace(tzinfo=None) + timedelta(seconds=time.timezone)
        return local_time

    @staticmethod
    def localtime_to_milliseconds(local_time):
        utc_time = local_time - timedelta(seconds=time.timezone)
        milliseconds = int((utc_time - datetime(1970, 1, 1)).total_seconds() * 1000)
        return milliseconds

    @staticmethod
    def current_time_to_milliseconds():
        current_time_seconds = time.time()
        return int(current_time_seconds * 1000)


converter = TimeConverter()

url = "https://api.hyperliquid.xyz/info"
payload = {
    "type": "fundingHistory",
    "coin": "TIA",
    "startTime": converter.current_time_to_milliseconds() - (60 * 60 * 1000),
}
headers = {"Content-Type": "application/json"}
res = requests.post(url, data=json.dumps(payload), headers=headers)
data = res.json()

for i, each in enumerate(reversed(data)):
    print(
        f"--{converter.milliseconds_to_localtime(each['time'])}--\nCoin: {each['coin']}\nFunding Rate: {round(float(each['fundingRate'])*100, 4)}\nPremium: {each['premium']}\n\n"
    )
