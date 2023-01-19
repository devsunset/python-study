import os
import shutil

path = r"C:\일잘러 파이썬과 40개의 작품들 코드\15.폴더내 모든파일 이동 프로그램 만들기\폴더1"
move_path = r"C:\일잘러 파이썬과 40개의 작품들 코드\15.폴더내 모든파일 이동 프로그램 만들기\폴더2"

for dirpath, dirname, files in os.walk(path):
    for filename in files:
        try:
            print(os.path.join(dirpath, filename))
            shutil.move(os.path.join(dirpath, filename), move_path)
        except:
            pass