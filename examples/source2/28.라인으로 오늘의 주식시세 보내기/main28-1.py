import requests

LINE_TOKEN = 'ypVP5seUvHQe67QcZWaqLImYcs3OP4SIkzLTTKGUh8X'

def send_line_message(token,message):
    try:
        TARGET_URL = 'https://notify-api.line.me/api/notify'
        headers={'Authorization': 'Bearer ' + token}
        data = {'message' : message}
        
        response = requests.post(TARGET_URL,headers=headers,data=data)
        if response.status_code == 200:
            return "전송 성공"
        else:
            return "전송 실패"
    except:
        return "에러"

print(send_line_message(LINE_TOKEN,"파이썬으로 보내는 메시지 입니다."))