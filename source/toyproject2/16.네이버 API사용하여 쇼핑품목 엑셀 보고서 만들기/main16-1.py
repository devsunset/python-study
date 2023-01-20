import urllib.request
import json

#애플리케이션 클라이언트 id 및 secret
client_id = "a0XLmXSasINGWGdq3D8b" 
client_secret = "kRL4Ulaxhr"

search_item = "썬크림"

def get_naver_shopping_items(item,id,secret):
    #쿼리작성
    url = "https://openapi.naver.com/v1/search/shop.json"
    option = "&display=10&start=1&sort=sim"
    query = "?query="+ urllib.parse.quote(search_item)
    url_query = url + query + option

    #Open API 검색 요청 개체 설정
    request = urllib.request.Request(url_query)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)

    #검색 요청 및 처리
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode == 200):
        response_body = response.read()
        return response_body.decode('utf-8')
    else:
        return None

응답결과 = get_naver_shopping_items(search_item, client_id, client_secret)

응답결과_json = json.loads(응답결과)
print(응답결과_json["items"][0:2])