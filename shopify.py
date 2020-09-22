####
## Shopify
####

#!/usr/bin/env python3

import config

import datetime
import time
import requests
import json
import re
import argparse


def get_unfulfilled():
    response = requests.get(
        "https://"
        + config.shopify["API_Key"]
        + ":"
        + config.shopify["API_Secret"]
        + "@"
        + config.shopify["shopify_base"]
        + config.shopify["count_endpoint"]
    )
    if response.status_code == 200:
        res_dict = response.json()
        return res_dict["count"]
    else:
        print("Error code: ")
        print(response.status_code)


def get_revenue():

    # Get current day
    d = datetime.datetime.today()

    response = requests.get(
        "https://"
        + config.shopify["API_Key"]
        + ":"
        + config.shopify["API_Secret"]
        + config.shopify["shopify_base"]
        + config.shopify["orders_endpoint"]
        + "?created_at_min="
        + str(d.year)
        + "-"
        + str(d.month)
        + "-"
        + str(d.day)
        + "T00:00:00-00:00&financial_status=paid&fields=total-price"
    )
    if response.status_code == 200:
        res_dict = json.loads(response.text)
        total = 0

        for item in res_dict["orders"]:
            for val in item.values():
                total += float(val)

        # printing sum
        return int(total)
    else:
        print("Error code: ")
        print(response.status_code)
