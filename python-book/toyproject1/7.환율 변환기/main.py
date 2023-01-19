# pip install currencyconverter
from currency_converter import CurrencyConverter
import requests
from bs4 import BeautifulSoup

cc = CurrencyConverter()
print(cc.currencies)

print("=====================================")

cc = CurrencyConverter('http://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip')
print(cc.convert(1,'USD','KRW'))

print("=====================================")

def get_exchange_rate():
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Content-Type': 'text/html; charset=utf-8'
    }

    response = requests.get("https://www.kita.net/cmmrcInfo/ehgtGnrlzInfo/rltmEhgt.do", headers=headers)
    content = BeautifulSoup(response.content, 'html.parser')
    containers = content.find('div', {'class': 'tableSt st4 alc'})
    print(containers)


get_exchange_rate()