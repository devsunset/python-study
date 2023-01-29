from PIL import  Image, ImageDraw, ImageFont

#이미지 불러오기 및 이미지사이즈 획득
image = Image.open('original.jpg')
width, height = image.size

#이미지 그리기
draw = ImageDraw.Draw(image)
text = "워터마크 테스트"

#폰트 설정 및 폰트사이즈 획득
font = ImageFont.truetype('NanumGothic.ttf', 30)
tw, th = font.getsize(text)

#중앙 좌표 얻기
x = int((width/2) - (tw/2))
y = int((height/2) - (th/2))

#워터마트 쓰기 및 이미지보여주기
draw.text((x, y), text, font=font)
image.show()