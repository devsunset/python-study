import requests
import re

url = "http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson?serviceKey=fFWLxGIoKo8cQCIuS5Is1fVoiKXkdls%2FU5DSGRwzmbiwIBI0nlz5V6jllexlrGLKR9y8wV3E3i0SMPTLtAhyvw%3D%3D&pageNo=1&numOfRows=30&startCreateDt=20220818&endCreateDt=20220818"
response = requests.get(url)

gubun = re.findall(r'<gubun>(.+?)</gubun>',response.text)
incDec = re.findall(r'<incDec>(.+?)</incDec>',response.text)

print("지역:", gubun)
print("확진자수:", incDec)