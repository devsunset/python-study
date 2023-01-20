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

#2022.08.10~2022.08.15 까지 수정한 문서를 찾아 출력
for file_path in founds_list:
    ctime = os.path.getctime(file_path)
    if datetime.fromtimestamp(ctime) >= datetime(2022, 8, 10, 0, 0):
        if datetime.fromtimestamp(ctime) < datetime(2022, 8, 16, 0, 0):
            print(file_path,datetime.fromtimestamp(ctime))
