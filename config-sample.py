####
## Config
####

functionality = dict(enable_display="true", enable_tower="true", enable_emails="true")

shipstation = dict(
    API_Key="",
    API_Secret="",
    orders_endpoint="https://ssapi.shipstation.com/orders?orderStatus=awaiting_shipment",
    tag_endpoint="https://ssapi.shipstation.com/orders/addtag",
    # Safe shipping timeframe in hours
    ship_timeframe=48,
    # Tag ID for the urgent tag
    urgent_tag=103434,
    # Tag ID for out of stock tag
    nostock_tag=0,
    # Tag ID for email sent tag
    emailed_tag=0,
)

shopify = dict(
    API_Key="",
    API_Secret="",
    shopify_base="YOURSTORENAME.myshopify.com",
    count_endpoint="/admin/api/2020-01/orders/count.json?fulfillment_status=unfulfilled",
    orders_endpoint="/admin/api/2020-01/orders.json",
)

freshdesk = dict(
    API_Key="",
    freshdesk_base="YOURSTORENAME.freshdesk.com",
    outbound_email_endpoint="/api/v2/tickets/outbound_email",
    email_config_id="",
)

todoist = dict(
    token="", tasks_endpoint="https://api.todoist.com/rest/v1/tasks", project_id="",
)
