#!/usr/bin/env python3
"""
Shipping Stork
"""

__author__ = "Chris Loidolt"
__version__ = "0.1.0"
__license__ = "GNU 3.0"

import config

import shopify
import shipstation
import todoist
import freshdesk
import hardware

import time
from datetime import datetime, timedelta

####
## Main
####


def main():
    """ Main entry point of the app """
    while True:

        # Flag orders outside shipping window
        shipstation.getOrders()

        # Get unshipped order count and revenue
        if config.functionality["enable_display"] == "true":
            count = shopify.get_unfulfilled()
            revenue = shopify.get_revenue()

            # Update display
            hardware.updateDisplay(revenue, count)

        # Update status light tower
        if config.functionality["enable_tower"] == "true":
            hardware.updateLights(1)

        ## Sleep for a while to prevent excessive API calls
        time.sleep(600)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
