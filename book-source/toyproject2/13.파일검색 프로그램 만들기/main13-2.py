import os
from datetime import datetime

찾을폴더_경로 = r"C:\일잘러 파이썬과 40개의 작품들 코드"

founds_list = []
for (path, dir, files) in os.walk(찾을폴더_경로):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        if ext == '.xlsx' or ext == '.docx':
            founds_list.append("%s/%s" % (path, filename))

print("파일이름: ",founds_list[0])

ctime = os.path.getctime(founds_list[0])
print("만든시간: ",datetime.fromtimestamp(ctime))

mtime = os.path.getmtime(founds_list[0])
print("수정시간: ",datetime.fromtimestamp(mtime))

atime = os.path.getatime(founds_list[0])
print("마지막엑세스시간: ",datetime.fromtimestamp(atime))

file_size = os.path.getsize(founds_list[0])
print("파일크기: ",file_size)