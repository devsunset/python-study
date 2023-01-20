import os

찾을폴더_경로 = r"C:\일잘러 파이썬과 40개의 작품들 코드"

for (path, dir, files) in os.walk(찾을폴더_경로):
    print(path)
    for filename in files:
        print(filename)