import cryptocode
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

비밀번호 = "hello12345"

file_path = '비밀번호들.txt'
with open(file_path, 'r', encoding='UTF8') as f : 
    read_file = f.read()

복호화된_문자열 = cryptocode.decrypt(read_file,비밀번호)

with open(file_path, 'w', encoding='UTF8') as f : 
    f.write(복호화된_문자열)