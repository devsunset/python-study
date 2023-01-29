
import pandas as pd
import pandas_datareader as pdr
from datetime import datetime
from dateutil.relativedelta import relativedelta

# 코스피에서 종목 다운로드
def get_kospi():  
    download_link = 'http://kind.krx.co.kr/corpgeneral/corpList.do' 
    download_link = download_link + '?method=download'  
    download_link = download_link + '&marketType=' + "stockMkt"  
    df = pd.read_html(download_link, header=0)[0]  
    df.종목코드 = df.종목코드.map('{:06d}.KS'.format) 
    return df

# kospi종목코드 다운로드
kospi_df = get_kospi()
kospi_df


# 10년전부터 지금까지 주식데이터 획득
now = datetime.now()

before = now - relativedelta(years=10)

now_day = now.strftime("%Y-%m-%d")
befor_day = before.strftime("%Y-%m-%d")
print(f"end  : {now_day}")
print(f"start: {befor_day}")

회사이름_list = kospi_df["회사명"].to_list()
종목코드_list = kospi_df["종목코드"].to_list()

tmp_df = pdr.get_data_yahoo(종목코드_list[0], start=befor_day, end=now_day)
tmp_df


# 10개의 종목에서 데이터 획득
stock_df = pd.DataFrame()
for i,회사이름 in enumerate(회사이름_list):
    tmp_df = pdr.get_data_yahoo(종목코드_list[i], start=befor_day, end=now_day)
    stock_df[회사이름] = tmp_df["Close"]
    if i >= 10:
        break;

stock_df



# 빈값을 채우기
stock_df = stock_df.fillna(method='backfill')

stock_df



#수익률 계산
수익률_df = pd.DataFrame()
수익률_df = stock_df.iloc[0] / stock_df.iloc[-1] * 100

수익률_df



#설치된 폰트 확인
import matplotlib.font_manager as fonm

font_list = [font.name for font in fonm.fontManager.ttflist]
for f in font_list:
    if "Nanum" in f:
        print(f)



#폰트설정
import matplotlib as mat
mat.rcParams['font.family'] = 'NanumGothic'

# 그래프 그리기
수익률_df.plot.bar(rot=270)

