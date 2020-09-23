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


def emailNoStock(email, orderNumber):

    payload = (
        '{\r\n    "description": "Shipping issue for order "'
        + orderNumber
        + ',\r\n    "subject": "Shipping issue for order '
        + orderNumber
        + '",\r\n    "email": "'
        + email
        + '",\r\n    "priority": 1,\r\n    "email_config_id": '
        + config.freshdesk["email_config_id"]
        + '" ,\r\n    ]\r\n}'
    )

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Basic %s" % createAuth(),
    }

    response = requests.request(
        "POST",
        "https://"
        + config.freshdesk["freshdesk_base"]
        + config.freshdesk["outbound_email_endpoint"],
        headers=headers,
        data=payload,
    )

    print(response.text.encode("utf8"))

