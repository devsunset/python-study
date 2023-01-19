import cv2
import numpy as np
from glob import glob
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

img_path = r'원본이미지'
img_list = glob(img_path + '\*.jpg')
img_list.extend(glob(img_path + '\*.png'))

img_array= []
for i,img in enumerate(img_list):
    img_read = np.fromfile(img, np.uint8)
    img_array.append(cv2.imdecode(img_read, cv2.IMREAD_COLOR))
    img_array[i] = cv2.resize(img_array[i],(480,360))
    
addv = cv2.vconcat(img_array)

cv2.imwrite('save.jpg',addv)