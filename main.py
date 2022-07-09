import datetime
import os
import re
import time
import requests
from ebaysdk.exception import ConnectionError
from ebaysdk.finding import Connection
from ebaysdk import config
import tabulate
from ebaysdk.shopping import Connection as Shopping

API_ID = "XYZ"
API_KEY_NOTIFY = "XYZ"



class Search:
    def __init__(self, query, min_val, max_val):
        self.query = query
        self.results = []
        self.min = min_val
        self.max = max_val
        self.update_results()

    def update_results(self):
        try:
            api = Connection(appid=API_ID, config_file=None, domain="svcs.ebay.de",
                             siteid="EBAY-DE")
            response = api.execute('findItemsAdvanced', {'keywords': self.query})
            data = []
            for item in response.reply.searchResult.item:
                temp = []
                temp.extend([item.title, item.condition.conditionDisplayName, item.listingInfo.listingType,
                             item.sellingStatus.currentPrice.value, item.viewItemURL, item.sellingStatus.timeLeft])
                data.append(temp)
            self.results = data
        except ConnectionError as e:
            print(e)
            print(e.response.dict())

    def get_best_match(self):
        match = []
        for result in self.results:

            if self.min <= float(result[3]) <= self.max:
                match.append(result)
                if result[2] == 'Auction' and remain_time(result[-1], 30):
                    send_notification(result[0], str(result), result[-2])
        return match


def remain_time(text, minutes):
    vals = [int(x) for x in re.findall(r"(?<=[A-Z])\d{1,2}", text)]
    if vals[0] == 0 and vals[1] == 0 and vals[2] > minutes:
        return True


def send_notification(title, message, link):
    requests.get(f"http://xdroid.net/api/message?k={API_KEY_NOTIFY}&t={title}&c={message}&u={link}")


