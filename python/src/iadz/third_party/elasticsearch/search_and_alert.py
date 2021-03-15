# -*- coding: utf-8 -*-

import os

import requests


ELASTICSEARCH_URI = "http://localhost:9200/test/_search"

SLACK_ROBOT_URI = os.getenv("SLACK_ROBOT_URL")

QUERY_STATEMENT = {
    "query": {"range": {"context_date": {"gte": "now-60m", "lt": "now"}}}
}


def query_alerts_by_datetime():

    response = requests.get(ELASTICSEARCH_URI, json=QUERY_STATEMENT)

    return response.json()["hits"]["hits"]


def send_alert_to_slack():

    result = query_alerts_by_datetime()

    for message in result:

        alert = message["_source"]["context_message"]

        payload = {
            "channel": "#platform_alerts",
            "username": "video-syncer",
            "text": alert,
            "icon_emoji": ":ghost:",
        }

        response = requests.post(SLACK_ROBOT_URI, json=payload)

        print(f"Notify #platform_alerts with: {alert}\nResponse: {response.content}")


if __name__ == "__main__":
    send_alert_to_slack()
