import cv2
import numpy as np

img1_path = 'image1.jpg'
img2_path = 'image2.jpg'

#이미지 읽기
img1_read = np.fromfile(img1_path, np.uint8)
img2_read = np.fromfile(img2_path, np.uint8)
img1= cv2.imdecode(img1_read, cv2.IMREAD_COLOR)
img2= cv2.imdecode(img2_read, cv2.IMREAD_COLOR)

# 사이즈 조절
img1 = cv2.resize(img1,(480,360))
img2 = cv2.resize(img2,(480,360))

# 이미지 붙이기
addv = cv2.vconcat([img1, img2])
addh = cv2.hconcat([img1, img2])

# 이미지 보이기
cv2.imshow('imgv',addv)
cv2.imshow('imgh',addh)

cv2.waitKey(0)
cv2.destroyAllWindows()