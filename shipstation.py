####
## Shipstation
####

#!/usr/bin/env python3

import config
import todoist
import freshdesk
import hardware

import requests
import json
import re
import argparse
import uuid
import base64
from datetime import datetime, timedelta


def createAuth():
    # Create base 64 header auth
    userpass = config.shipstation["API_Key"] + ":" + config.shipstation["API_Secret"]
    encoded_u = base64.b64encode(userpass.encode()).decode()

    return encoded_u


def getOrders():
    headers = {"Authorization": "Basic %s" % createAuth()}
    payload = {}

    # Get unshipped orders from shipstation
    response = requests.get(
        config.shipstation["orders_endpoint"], headers=headers, data=payload
    )

    if response.status_code == 200:
        res_dict = response.json()
        filterOrders(res_dict)
    else:
        print("Error code: ")
        print(response.status_code)


def filterOrders(orders):
    # Iterate through orders
    if orders != []:
        for index in range(len(orders["orders"])):
            # Check if order notes contain an amazon order ID
            notes = str(orders["orders"][index]["customerNotes"])
            if "Amazon Order ID:" in notes:
                print(orders["orders"][index]["orderNumber"])
                # Get order date and current timestamp
                orderDate = datetime.strptime(
                    str(orders["orders"][index]["orderDate"]), "%Y-%m-%dT%H:%M:%S.%f0"
                )
                currentDate = datetime.now()
                # Check if order creation date is outside shipping timeframe
                difference = currentDate - orderDate
                timeframe = timedelta(hours=config.shipstation["ship_timeframe"])
                if difference > timeframe:
                    # Add urgent tag in shipstation
                    tagUrgent(orders["orders"][index]["orderId"])
                    # Create task in todoist
                    todoist.checkExisting(orders["orders"][index]["orderNumber"])
                else:
                    print("Inside shipping window")

            # Check if order is tagged as no stock
            tags = str(orders["orders"][index]["tagIds"])
            if config.shipstation["nostock_tag"] in tags:
                print("No stock order found")
                # Check if email was already sent
                if config.shipstation["emailed_tag"] in tags:
                    print("Ticket already created")
                else:
                    # Send no inventory notification email
                    print("Creating no stock notification ticket")
                    createdTicket = freshdesk.noStockTicket(
                        orders["orders"][index]["customerEmail"],
                        orders["orders"][index]["orderNumber"],
                    )
                    if createdTicket == 1:
                        print("Tagging order as email sent")
                        tagEmailSent(orders["orders"][index]["orderId"])

            # Check if order is tagged thru-hiker
            tags = str(orders["orders"][index]["tagIds"])
            if config.shipstation["thruhiker_tag"] in tags:
                print("Thru-Hiker order found")
                # Create task in todoist
                # todoist.checkExistingThruHiker(orders["orders"][index]["orderNumber"])

        # Check if any order is tagged urgent
        # Update status light tower
        if config.functionality["enable_tower"] == "true":
            allOrders = str(orders["orders"])
            if config.shipstation["urgent_tag"] in allOrders:
                hardware.updateLights(2)
            else:
                hardware.updateLights(0)

    else:
        print("No Orders")


def tagUrgent(orderId):
    headers = {"Authorization": "Basic %s" % createAuth()}
    payload = {"orderId": orderId, "tagId": config.shipstation["urgent_tag"]}

    # Get unshipped orders from shipstation
    response = requests.post(
        config.shipstation["tag_endpoint"], headers=headers, json=payload
    )

    if response.status_code == 200:
        print("Order " + str(orderId) + " tagged as urgent")
        return
    else:
        print("Error code: ")
        print(response.status_code)
        return


def tagEmailSent(orderId):
    headers = {"Authorization": "Basic %s" % createAuth()}
    payload = {"orderId": orderId, "tagId": config.shipstation["emailed_tag"]}

    # Get unshipped orders from shipstation
    response = requests.post(
        config.shipstation["tag_endpoint"], headers=headers, json=payload
    )

    if response.status_code == 200:
        print("Order " + str(orderId) + " tagged email sent")
        return
    else:
        print("Error code: ")
        print(response.status_code)
        return
