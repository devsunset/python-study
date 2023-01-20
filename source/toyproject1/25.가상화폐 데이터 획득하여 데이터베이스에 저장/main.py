# https://github.com/sharebook-kr/pyupbit
# pip install pyupbit
# https://sqlitebrowser.org/dl

import pyupbit
import pandas as pd
import sqlite3
import datetime

coin_lists = pyupbit.get_tickers(fiat='KRW')
print(coin_lists)

print("=====================================")

price_now = pyupbit.get_current_price(["KRW-BTC", "KRW-ETH"])
print(price_now)

print("=====================================")

ticker = 'KRW-BTC'
interval = 'minute1'
to = '2023-01-20 11:00'
count = 200
price_now = pyupbit.get_ohlcv(ticker=ticker,interval=interval,to=to,count=count)

db_path = "coin.db"

con = sqlite3.connect(db_path, isolation_level=None)
price_now.to_sql('BTC', con, if_exists='append')

con.close

print("=====================================")

db_path = "coin.db"
con = sqlite3.connect(db_path, isolation_level=None)

readed_df = pd.read_sql("SELECT * FROM 'BTC'", con, index_col = 'index')

print(readed_df)

print("=====================================")
def date_range(start, end):
    start = datetime.datetime.strptime(start, "%Y-%m-%d")
    start = start + datetime.timedelta(days=1)
    end = datetime.datetime.strptime(end, "%Y-%m-%d")
    end = end + datetime.timedelta(days=1)
    dates = [(start + datetime.timedelta(days=i)).strftime("%Y-%m-%d") for i in range((end-start).days+1)]
    return dates

dates = date_range("2023-01-01", "2023-01-15")

print(dates)

for day in reversed(dates):
    myDay = day + ' 00:00'
    print(myDay)

    ticker = 'KRW-BTC'
    interval = 'minute1'
    to = myDay
    count = 1440
    price_now = pyupbit.get_ohlcv(ticker=ticker,interval=interval,to=to,count=count)

    print(price_now)

    db_path = "coin.db"

    con = sqlite3.connect(db_path, isolation_level=None)
    price_now.to_sql('BTC', con, if_exists='append')

    con.close

print("=====================================")

db_path = "coin.db"
con = sqlite3.connect(db_path, isolation_level=None)

readed_df = pd.read_sql("SELECT DISTINCT * FROM 'BTC'", con, index_col = 'index')

readed_df.to_sql('BTC_NEW', con, if_exists='replace')

print(readed_df)