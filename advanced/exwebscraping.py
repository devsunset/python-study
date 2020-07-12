# $ pip install requests
# $ pip install beautifulsoup4
# $ pip install scrapy

# scraping 여부 확인
# http://.../robots.txt)

import requests, bs4

# case 1

# Proxy info
http_proxy  = "http://xxx.xxx.xxx.xxx:xxxx"
https_proxy = "https://xxx.xxx.xxx.xxx:xxxx"

proxyDict = { 
              "http"  : http_proxy, 
              "https" : https_proxy
            }

# get
resp = requests.get('http://httpbin.org/get)
# resp = requests.get('http://httpbin.org/get',proxies=proxyDict)
print(resp.text) 

# post
dic = {"id": 1, "name": "kang", "age": 10}
resp = requests.post('http://httpbin.org/post')
# resp = requests.post('http://httpbin.org/post', data=dic,proxies=proxyDict)
print(resp.text)

# put 
resp = requests.put('http://httpbin.org/put')
# resp = requests.put('http://httpbin.org/put',proxies=proxyDict)
print(resp.text)

# delete
resp = requests.delete('http://httpbin.org/delete')
# resp = requests.delete('http://httpbin.org/delete',proxies=proxyDict)
print(resp.text)


resp = requests.get('http://www.apache.org/') 
# resp = requests.get('http://www.apache.org/',proxies=proxyDict)
resp.raise_for_status()
 #resp.encoding='euc-kr'
html = resp.text

bs = bs4.BeautifulSoup(html, 'html.parser')
tags = bs.select('ul.dropdown-menu li a') 

for i in range(len(tags)):
    txt = tags[i].getText()
    print(txt)


# case 2 - NAVER 파이썬  검색 결과  - 블로그 리스트 제목과 주소 얻기 
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

baseUrl = 'https://search.naver.com/search.naver?where=post&sm=tab_jum&query='
plusUrl = input('검색어를 입력하세요.')

url = baseUrl + urllib.parse.quote_plus(plusUrl)
url = 'https://search.naver.com/search.naver?where=post&sm=tab_jum&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC'

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,'html.parser')
print(soup)

title = soup.find_all(class_='sh_blog_title')

for i in title:
  print(i.attrs['title'])
  print(i.attrs['href'])


# case 3 - NAVER 검색 이미지 다운로드
from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup

baseUrl = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
plusUrl = input('검색어를 입력하세요.')
url = baseUrl + urllib.parse.quote_plus(plusUrl)

html = urlopen(url).read()
soup = BeautifulSoup(html,'html.parser')

img = soup.find_all(class_='_img')
print(img[0])

for x in img:
  imgUrl = x['data-source']
  with urlopen(imgUrl) as f:
    with open(plusUrl+str(n)+'.jpg','wb') as h:
      img = f.read()
      h.write(img)

  n +=1

print('다운로드 완료')




# case 4 - scrapy

# scrapy shell
# fetch('http://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=001')
# view(response)
# print(response.text)
# response.xpath('//*[@id="main_content"]/div[2]/ul/li/dl/dt[2]/a/text()').extract()
# response.css('.writing::text').extract()
# response.css('.lede::text').extract()

# -------------------------------------------------------------------------------

# scrapy startproject naverscraper

# scrapy genspider newsbot news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=001


# newsbot.py
# import scrapy

# class NewsbotSpider(scrapy.Spider):
# 	name = 'newsbot'
# 	start_urls = ['http://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=001']

# 	def parse(self, response):
# 		titles = response.xpath('//*[@id="main_content"]/div[2]/ul/li/dl/dt[2]/a/text()').extract()
# 		authors = response.css('.writing::text').extract()
# 		previews = response.css('.lede::text').extract()

# 		for item in zip(titles, authors, previews):
# 			scraped_info = {
# 				'title' : item[0].strip(),
# 				'author' : item[1].strip(),
# 				'preview' : item[2].strip(),
# 			}
# 			yield scraped_info



# scrapy crawl newsbot

# settings.py
# FEED_FORMAT = "csv"
# FEED_URI = "naver_news.csv"

# scrapy crawl newsbot