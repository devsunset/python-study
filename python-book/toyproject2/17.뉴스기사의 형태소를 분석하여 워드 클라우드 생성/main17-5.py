import requests
import re
import xml.etree.ElementTree as ET
from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud

okt = Okt()

url = 'https://news.google.com/rss?hl=ko&gl=KR&ceid=KR:ko' 

headers = {
        'User-Agent': 'Mozilla/5.0',
        'Content-Type': 'text/html; charset=utf-8'
        }

response = requests.get(url, headers=headers)

root_element = ET.fromstring(response.text)
iter_element = root_element.iter(tag="item") 

title_list = []
description_list = []
for element in iter_element:
    title_list.append(element.find("title").text)
    hangul = re.compile('[^ ㄱ-ㅣ가-힣]+')
    description = element.find("description").text
    description_list.append(hangul.sub("",description))

명사_list = []
for title in title_list:
    for 명사 in okt.nouns(title):
        if len(명사) > 1:
            명사_list.append(명사)

for description in description_list:
    for 명사 in okt.nouns(description):
        if len(명사) > 1:
            명사_list.append(명사)

명사_빈도수_list = Counter(명사_list)

wc = WordCloud(font_path="NanumGothic", width=400, height=400, scale=2.0, max_font_size=250)
gen = wc.generate_from_frequencies(명사_빈도수_list)
wc.to_file(r'17.뉴스기사의 형태소를 분석하여 워드 클라우드 생성\뉴스_워드클라우드.png')