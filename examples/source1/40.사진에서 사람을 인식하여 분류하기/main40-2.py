# pip install torch==1.9.0
# pip install torchvision=0.10.0
import torch
from glob import glob

img_path = '원본이미지'

img_list = glob(img_path + '\*.jpg')
img_list.extend(glob(img_path + '\*.png'))

print(img_list)

model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

for img_path in img_list:
    results = model(img_path)
    print(img_path)
    results.save("이미지확인용")
    for pred in results.pred[0]:
        tag = results.names[int(pred[-1])] 
        print(tag)