import requests
from bs4 import BeautifulSoup
import schedule
import time


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

def get_kospi_kosdaq_now():
    url = 'https://finance.naver.com/sise/'
    response = requests.get(url)
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        kospi = soup.select_one('#KOSPI_now')
        kosdaq = soup.select_one('#KOSDAQ_now')
        return kospi.text, kosdaq.text
    else : 
        return "에러"

def send_mesaage():
    kospi_now, kosdaq_now = get_kospi_kosdaq_now()
    send_message = "코스피: " + kospi_now + " 코스닥: " + kosdaq_now
    print(send_line_message(LINE_TOKEN,send_message))

schedule.every().monday.at("09:10").do(send_mesaage)
schedule.every().tuesday.at("09:10").do(send_mesaage)
schedule.every().wednesday.at("09:10").do(send_mesaage)
schedule.every().thursday.at("09:10").do(send_mesaage)
schedule.every().friday.at("09:10").do(send_mesaage)

while True:
    schedule.run_pending()
    time.sleep(1.0)