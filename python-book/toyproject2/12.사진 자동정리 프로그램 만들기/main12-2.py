from PIL import Image
from PIL.ExifTags import TAGS
from glob import glob

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

사진들 = (glob(r'사진\*.jpg'))
사진들.extend(glob(r'사진\*.png'))

image = Image.open(사진들[0])
info = image._getexif();
image.close()

taglabel = {}
for tag, value in info.items():
    decoded = TAGS.get(tag, tag)
    taglabel[decoded] = value

for 사진 in 사진들:
    image = Image.open(사진)
    info = image._getexif();
    image.close()

    taglabel = {}
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        taglabel[decoded] = value
        
    print("사진이름: ",사진)
    print("사진촬영시간: ",taglabel['DateTime'])
    print("사진촬영장소: ",taglabel['GPSInfo'])