####
## Freshdesk
####

#!/usr/bin/env python3

import config

import requests
import base64


def createAuth():
    # Create base 64 header auth
    userpass = config.freshdesk["API_Key"] + ":X"
    encoded_u = base64.b64encode(userpass.encode()).decode()

    return encoded_u


def noStockTicket(email, orderNumber):

    payload = {
        "description": "Order "
        + orderNumber
        + " was tagged as unable to ship due to insufficent on hand inventory. An agent will contact you shortly with next steps and alternate options. Our apologies for the inconvienience. We do our best to keep inventory values up to date online but occasionally mistakes are made or a selling channel doesn't update in time allowing an item to be oversold.",
        "subject": "Insufficent Inventory for Order " + orderNumber,
        "email": email,
        "priority": 1,
        "status": 2,
        "cc_emails": [],
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Basic %s" % createAuth(),
    }

    response = requests.post(
        "https://"
        + config.freshdesk["freshdesk_base"]
        + config.freshdesk["create_ticket_endpoint"],
        headers=headers,
        json=payload,
    )

    if response.status_code == 201:
        print("Ticket Created")
        return 1
    else:
        print("Error code: ")
        print(response.status_code)
        return 0

