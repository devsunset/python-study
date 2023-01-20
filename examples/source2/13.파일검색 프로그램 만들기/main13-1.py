import os

찾을폴더_경로 = r"C:\일잘러 파이썬과 40개의 작품들 코드"

founds_list = []
for (path, dir, files) in os.walk(찾을폴더_경로):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        if ext == '.xlsx' or ext == '.docx':
            founds_list.append("%s/%s" % (path, filename))

try:
    print(founds_list[0:5])
except:
    print(founds_list)