import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from rembg import remove

input_path = 'image.jpg'
output_path = "out_" + input_path

with open(input_path, 'rb') as i:
    with open(output_path, 'wb') as o:
        input = i.read()
        output = remove(input)
        o.write(output)