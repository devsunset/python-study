import requests
import json


# slack_webhook_url = "https://hooks.slack.com/services/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"

slack_webhook_url = "https://hooks.slack.com/services/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"

def sendSlackWebhook(strText):
    headers = {
    "Content-type": "application/json"
    }

    data = {
        "text" : strText
    }

    res = requests.post(slack_webhook_url, headers=headers, data=json.dumps(data))
    
    if res.status_code == 200:
        return "ok"
    else:
        return "error"

print(sendSlackWebhook("Hello World"))