import os
from datetime import datetime

찾을폴더_경로 = r"C:\일잘러 파이썬과 40개의 작품들 코드"

#.xlsx 엑셀파일과 .docx 워드파일을 찾음
founds_list = []
for (path, dir, files) in os.walk(찾을폴더_경로):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        if ext == '.xlsx' or ext == '.docx':
            founds_list.append("%s/%s" % (path, filename))

#파일의 크기가 10KBytes = 10000Bytes보다 큰파일 출력
for file_path in founds_list:
    file_size = os.path.getsize(file_path)
    if file_size > 10000:
        print(file_path, file_size, "Bytes")