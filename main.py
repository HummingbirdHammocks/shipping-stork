#!/usr/bin/env python3
"""
Shipping Stork
"""

__author__ = "Chris Loidolt"
__version__ = "0.1.0"
__license__ = "GNU 3.0"

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
    starttime = time.time()
    while True:

        # Flag orders outside shipping window
        shipstation.getOrders()

        # Get unshipped order count and revenue
        count = shopify.get_unfulfilled()
        revenue = shopify.get_revenue()

        # Update display
        hardware.updateDisplay(revenue, count)

        ## Sleep for a while to prevent excessive API calls
        time.sleep(30.0 - ((time.time() - starttime) % 60.0))


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
