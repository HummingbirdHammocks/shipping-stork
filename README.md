# Shipping Stork
Shipping system manager for a Shopify, Shipstation, Freshdesk, and Todoist based workflow.

This system performs the following functions:

- Update a dot matrix display with the last 24 hour's unshipped orders and revenue.
- Update a green/yellow/red light status tower with current shipping status.
- Add a task to Todoist if an Amazon order shipment in Shipstation will soon be late and mark order with Urgent tag.
- Send out of stock notification email to orders tagged as out of stock.

## How To Use

1. Ensure you have python3 installed and working correctly

2. Install requirements using the following command:

`pip3 install -r requirements.txt`

3. Copy config-sample.py to a new file called config.py. Populate with your Todoist API token and which project you want to add tasks to. You will also need to fill in your API details for shipstation as well as the ship timeframe and tag id.

4. Test by running the following from the project directory.

`python3 main.py`

5. Add to some type of scheduler to be sure it runs on a regular basis.
