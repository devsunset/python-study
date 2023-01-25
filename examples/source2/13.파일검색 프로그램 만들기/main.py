import os
from datetime import datetime

찾을폴더_경로 = "../../"

#.xlsx 엑셀파일과 .docx 워드파일을 찾음
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

print("=====================================")

#2022.08.10~2023.08.15 까지 수정한 문서를 찾아 출력
for file_path in founds_list:
    ctime = os.path.getctime(file_path)
    if datetime.fromtimestamp(ctime) >= datetime(2022, 8, 10, 0, 0):
        if datetime.fromtimestamp(ctime) < datetime(2023, 8, 16, 0, 0):
            print(file_path,datetime.fromtimestamp(ctime))

print("=====================================")

#최근 5일 이내에 생성된 파일만 출력하기
for file_path in founds_list:
    mtime = os.path.getmtime(file_path)
    days = datetime.now() - datetime.fromtimestamp(mtime)
    if days.days <= 5:
        print(file_path,datetime.fromtimestamp(mtime))

print("=====================================")

#파일의 크기가 10KBytes = 10000Bytes보다 큰파일 출력
for file_path in founds_list:
    file_size = os.path.getsize(file_path)
    if file_size > 10000:
        print(file_path, file_size, "Bytes")