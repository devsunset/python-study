import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# import subprocess, time
#
# file_path = 'test.txt'
# os.startfile(file_path)
#
# memo_proc = subprocess.Popen('notepad')
# time.sleep(5)
#
# if memo_proc.poll() == None:
#     print("메모장을 종료 합니다.")
#     memo_proc.kill()

import subprocess

subprocess.call('python print_hello.py', shell=True)
print("실행완료")