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

slack_webhook_url = "https://hooks.slack.com/services/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"

print(send_slack_webhook(slack_webhook_url,"SSS급 일잘러를 위한 파이썬과 40개의 작품들 입니다."))