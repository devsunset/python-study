import urllib.request
import json

client_id = "a0XLmXSasINGWGdq3D8b" 
client_secret = "kRL4Ulaxhr"

def get_naver_shorturl(long_url,id,secret):
    encText = urllib.parse.quote(long_url)
    data = "url=" + encText
    url = "https://openapi.naver.com/v1/util/shorturl"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",id)
    request.add_header("X-Naver-Client-Secret",secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        response_json = json.loads(response_body.decode('utf-8'))
        return response_json['result']['url']
    else:
        return "Error Code:" + rescode

my_url = "https://munjjac.tistory.com/11"
short_url = get_naver_shorturl(my_url,client_id,client_secret)
print(short_url)