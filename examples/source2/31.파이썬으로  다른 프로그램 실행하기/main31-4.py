import schedule
import subprocess
import time

def do_file_backup():
    backup_command = 'C:/Users/jang/anaconda3/python.exe "c:/일잘러 파이썬과 40개의 작품들 코드/10.파일 자동백업프로그램 만들기/main.py"'
    subprocess.call(backup_command, shell=True)
    print("백업프로그램 실행완료")

schedule.every(30).seconds.do(do_file_backup)

while True:
    schedule.run_pending()
    time.sleep(1.0)