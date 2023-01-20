from distutils.dir_util import copy_tree

원본_폴더 = r"C:\일잘러 파이썬과 40개의 작품들 코드\10.파일 자동백업프로그램 만들기\원본"
백업될_폴더 = r"C:\일잘러 파이썬과 40개의 작품들 코드\10.파일 자동백업프로그램 만들기\백업"
result = copy_tree(원본_폴더, 백업될_폴더,update=1)
print(result)