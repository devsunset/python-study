import requests
import re
import datetime

url = "http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson?serviceKey="
api_key = "fFWLxGIoKo8cQCIuS5Is1fVoiKXkdls%2FU5DSGRwzmbiwIBI0nlz5V6jllexlrGLKR9y8wV3E3i0SMPTLtAhyvw%3D%3D"

def get_today_covid19(url,api_key):
    now = datetime.datetime.now()
    yyyymmdd = now.strftime('%Y%m%d')
    
    page_no =  "&pageNo=1&numOfRows=30&"
    today = "startCreateDt=" + yyyymmdd + "&endCreateDt=" + yyyymmdd

    response = requests.get(url + api_key + page_no + today)

    gubun = re.findall(r'<gubun>(.+?)</gubun>',response.text)
    incDec = re.findall(r'<incDec>(.+?)</incDec>',response.text)

    return yyyymmdd,gubun,incDec

날짜, 지역, 확진자수 = get_today_covid19(url,api_key)

print("날짜:",날짜)
print("지역:",지역)
print("확진자수:",확진자수)