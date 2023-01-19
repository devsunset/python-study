from glob import glob

img_path = r'38.이미지에 워터마크 넣기\원본이미지'

img_list = glob(img_path + '\*.jpg')
img_list.extend(glob(img_path + '\*.png'))

print(img_list)