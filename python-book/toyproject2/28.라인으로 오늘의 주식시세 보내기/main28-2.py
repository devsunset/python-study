import requests
from bs4 import BeautifulSoup


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

kospi_now, kosdaq_now = get_kospi_kosdaq_now()

print("코스피: ",kospi_now)
print("코스닥: ",kosdaq_now)