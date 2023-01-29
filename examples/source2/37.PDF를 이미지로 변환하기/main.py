from pdf2image import convert_from_path
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

pdf_path = '2022-0001장다인.pdf'

poppler_bin_path = "...poppler-0.68.0\bin"
images = convert_from_path(pdf_path, poppler_path= poppler_bin_path)

for i, image in enumerate(images):
	image.save(pdf_path.split('.')[0]+str(i)+".jpg", "JPEG")