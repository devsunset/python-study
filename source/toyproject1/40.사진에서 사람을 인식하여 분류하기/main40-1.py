from glob import glob

img_path = '원본이미지'

img_list = glob(img_path + '\*.jpg')
img_list.extend(glob(img_path + '\*.png'))

print(img_list)