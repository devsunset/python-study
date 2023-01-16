import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import subprocess

subprocess.call('python print_hello.py', shell=True)
print("실행완료")