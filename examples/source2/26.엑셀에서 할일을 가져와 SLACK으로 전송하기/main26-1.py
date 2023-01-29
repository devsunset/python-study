import requests
import json


def send_slack_webhook(webhook_url,strText):
    headers = {
    "Content-type": "application/json"
    }

    data = {
        "text" : strText
    }

    res = requests.post(webhook_url, headers=headers, data=json.dumps(data))
    
    if res.status_code == 200:
        return "ok"
    else:
        return "error"

slack_webhook_url = "https://hooks.slack.com/services/"

print(send_slack_webhook(slack_webhook_url,"slack message send test"))