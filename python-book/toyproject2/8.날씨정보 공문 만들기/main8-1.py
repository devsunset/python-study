import requests
import re

url = "http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=4139054000"
response = requests.get(url)

요청시간 = re.findall(r'<pubDate>(.+)</pubDate>',response.text)
지역 = re.findall(r'<category>(.+)</category>',response.text)
날씨정보 = re.findall(r'<wfKor>(.+)</wfKor>',response.text)
시간 = re.findall(r'<hour>(.+)</hour>',response.text)
온도 = re.findall(r'<temp>(.+)</temp>',response.text)
습도 = re.findall(r'<reh>(.+)</reh>',response.text)

print("요청시간: ",요청시간)
print("지역: ",지역)
print("날씨정보: ",날씨정보)
print("시간: ",시간)
print("온도: ",온도)
print("습도: ",습도)