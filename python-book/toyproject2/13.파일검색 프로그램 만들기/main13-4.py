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

#최근 5일 이내에 생성된 파일만 출력하기
for file_path in founds_list:
    mtime = os.path.getmtime(file_path)
    days = datetime.now() - datetime.fromtimestamp(mtime)
    if days.days <= 5:
        print(file_path,datetime.fromtimestamp(mtime))