import pandas as pd
import time
import datetime
import requests
import json
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

slack_webhook_url = "https://hooks.slack.com/services/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"

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

while True:
    excel_file_path = '할일.xlsx'
    df_from_excel = pd.read_excel(excel_file_path)

    time_list = df_from_excel['시간'].tolist()
    todo_list = df_from_excel['할일'].tolist()

    now = datetime.datetime.now()
    print( now )
    for i,t in enumerate(time_list) :
        time_difference = t - now
        print(todo_list[i],time_difference)
        if time_difference.days >= 0 and time_difference.seconds <= 60:
            print(todo_list[i], " 메시지전송!!!")
            send_slack_webhook(slack_webhook_url,todo_list[i])
            time.sleep(61.0)
    time.sleep(1.0)