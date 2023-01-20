import subprocess, time

memo_proc = subprocess.Popen('notepad')
time.sleep(5)

if memo_proc.poll() == None:
    print("메모장을 종료 합니다.")
    memo_proc.kill()