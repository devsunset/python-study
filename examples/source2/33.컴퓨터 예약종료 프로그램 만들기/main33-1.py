import os
import time

#컴퓨터 끄기
os.system('shutdown -s -t 3600') 
time.sleep(5.0)

#취소
os.system('shutdown -a') 