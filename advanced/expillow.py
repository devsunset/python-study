# $ pip install Pillow

from PIL import Image

# Save as other type
im = Image.open('python-logo.png')
print(im.size)
im.save('python-logo.jpg')

# Thumbnail
im = Image.open('python.png')
size = (64, 64)
im.thumbnail(size)   
im.save('python-thumb.jpg')

# Crop
im = Image.open('python.png')
cropImage = im.crop((100, 100, 150, 150))
cropImage.save('python-crop.jpg')

# Resize & Rotate
im = Image.open('python.png')
 
# 크기를 600x600 으로
img2 = im.resize((600, 600))
img2.save('python-600.jpg')
 
# 90도 회전
img3 = im.rotate(90)
img3.save('python-rotate.jpg')

# filter
from PIL import Image, ImageFilter
 
im = Image.open('python.png')
blurImage = im.filter(ImageFilter.BLUR)
blurImage.save('python-blur.png')