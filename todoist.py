####
## Todoist
####

#!/usr/bin/env python3

import config

import requests
import json
import re
import argparse
import uuid
import base64
from datetime import datetime, timedelta


def checkExisting(orderNumber):
    headers = {
        "Authorization": "Bearer %s" % config.todoist["token"],
        "Content-Type": "application/json",
    }

    payload = {}

    # Get current tasks for project
    response = requests.get(
        config.todoist["tasks_endpoint"]
        + "?project_id="
        + config.todoist["project_id"],
        headers=headers,
        data=payload,
    )

    # Check if task exists
    if response.status_code == 200:
        tasks_string = response.text

        if tasks_string:
            # Build task name string
            taskName = "Ship Amazon Order " + str(orderNumber) + " within 24 hours"

            # Check if task name exists in dictonary
            exists = taskName in tasks_string

            if exists:
                print("Task for " + str(orderNumber) + " exists, skipping")
            else:
                # If no matching task exists, create new task
                addTask(orderNumber)
        else:
            print("No Tasks")
    else:
        print("Error code: ")
        print(response.status_code)


def addTask(orderNumber):
    headers = {
        "Authorization": "Bearer %s" % config.todoist["token"],
        "Content-Type": "application/json",
    }

    payload = (
        '{\r\n    "content": "Ship Amazon Order '
        + str(orderNumber)
        + ' within 24 hours",\r\n    "project_id":'
        + config.todoist["project_id"]
        + ',\r\n    "due_string": "now",\r\n    "due_lang": "en",\r\n    "priority": 4\r\n}'
    )

    # Create task in todoist
    response = requests.post(
        config.todoist["tasks_endpoint"], headers=headers, data=payload,
    )

    if response.status_code == 200:
        print("Todoist task added for order " + str(orderNumber))
    else:
        print("Error code: ")
        print(response.status_code)


def checkExistingThruHiker(orderNumber):
    headers = {
        "Authorization": "Bearer %s" % config.todoist["token"],
        "Content-Type": "application/json",
    }

    payload = {}

    # Get current tasks for project
    response = requests.get(
        config.todoist["tasks_endpoint"]
        + "?project_id="
        + config.todoist["project_id"],
        headers=headers,
        data=payload,
    )

    # Check if task exists
    if response.status_code == 200:
        tasks_string = response.text

        if tasks_string:
            # Build task name string
            taskName = "Thru Hiker Order " + str(orderNumber)

            # Check if task name exists in dictonary
            exists = taskName in tasks_string

            if exists:
                print("Task for " + str(orderNumber) + " exists, skipping")
            else:
                # If no matching task exists, create new task
                addTaskThruHiker(orderNumber)
        else:
            print("No Tasks")
    else:
        print("Error code: ")
        print(response.status_code)


def addTaskThruHiker(orderNumber):
    headers = {
        "Authorization": "Bearer %s" % config.todoist["token"],
        "Content-Type": "application/json",
    }

    payload = (
        '{\r\n    "content": "Thru Hiker Order '
        + str(orderNumber)
        + '",\r\n    "project_id":'
        + config.todoist["project_id"]
        + ',\r\n    "due_string": "now",\r\n    "due_lang": "en",\r\n    "priority": 4\r\n}'
    )

    # Create task in todoist
    response = requests.post(
        config.todoist["tasks_endpoint"], headers=headers, data=payload,
    )

    if response.status_code == 200:
        print("Todoist task added for order " + str(orderNumber))
    else:
        print("Error code: ")
        print(response.status_code)
