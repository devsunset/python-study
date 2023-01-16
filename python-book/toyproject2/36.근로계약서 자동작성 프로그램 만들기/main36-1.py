from PIL import Image, ImageDraw, ImageFont 
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

text = "테스트 입니다."

empty_im = Image.new("RGB", (2480, 3508), "white")

draw=ImageDraw.Draw(empty_im) 
draw.text((300,300)
          ,text
          ,font=ImageFont.truetype("NanumGothic", 60)
          ,fill=(0,0,0)) 

empty_im.save("test.png")