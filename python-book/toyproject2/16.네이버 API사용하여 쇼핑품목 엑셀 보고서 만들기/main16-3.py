import urllib.request
import json
import pandas as pd
import urllib.request as req
from io import BytesIO
import PIL
from openpyxl import Workbook
from openpyxl import load_workbook
from openpyxl.drawing.image import Image
from openpyxl.styles import Alignment
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

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

df = pd.DataFrame(응답결과_json["items"])

df.to_excel('네이버쇼핑_리스트.xlsx')

#엑셀파일을 openpyxl 라이브러리를 이용하여 불러옴
wb = load_workbook('네이버쇼핑_리스트.xlsx')
ws  = wb.active

#사진이 저장될 D행의 가로길이를 늘림
ws.column_dimensions["D"].width = 15

#이미지를 엑셀에 삽입
image_url_list = df["image"].to_list()
for i,image_url in enumerate(image_url_list):
    #이미지를 읽어와 크기를 변경하고 이미지를 저장
    img_data = PIL.Image.open(BytesIO(req.urlopen(image_url).read()))
    img_data = img_data.resize((100,100))
    img_name = image_url.split("/")[-1]
    img_data.save(img_name)
    
    #셀의 높이를 사진보다 높임
    ws.row_dimensions[i+2].height = 80
    img = Image(img_name)
    
    #이미지 넣기
    ws.add_image(img, "D"+ str(i+2))

#엑셀 저장
wb.save("네이버쇼핑_리스트_이미지.xlsx")

#저장된 이미지 삭제
for image_url in image_url_list:
    img_name = image_url.split("/")[-1]
    os.remove(img_name)