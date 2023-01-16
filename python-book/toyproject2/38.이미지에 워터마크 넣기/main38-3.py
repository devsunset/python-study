from glob import glob
from PIL import  Image, ImageDraw, ImageFont
import os

img_path = r'38.이미지에 워터마크 넣기\원본이미지'
water_img_path = r'38.이미지에 워터마크 넣기\워터마크이미지'

img_list = glob(img_path + '\*.jpg')
img_list.extend(glob(img_path + '\*.png'))

for img in img_list:
    image = Image.open(img)
    width, height = image.size

    draw = ImageDraw.Draw(image)
    text = "워터마크 테스트"

    font = ImageFont.truetype('NanumGothic.ttf', 30)
    tw, th = font.getsize(text)

    x = int((width/2) - (tw/2))
    y = int((height/2) - (th/2))

    draw.text((x, y), text, font=font)
    image.save(water_img_path + "\\" + os.path.basename(img))
    print("변환완료: ", img)