# OCR 프로그램 설치 - https://github.com/UB-Mannheim/tesseract/wiki
# pip install pytesseract

from PIL import Image
import pytesseract

image_path = "한글이미지.png"

# 사용 가능한 언어 확인
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
laguages = pytesseract.get_languages(config='')
print(laguages)


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' 
text = pytesseract.image_to_string(Image.open(image_path), lang="kor")
print(text)

with open("한글변환.txt", "w", encoding="utf8") as f:
    f.write(text)