import threading
import time

# 2가지 동작이 동시에 실행
def thread_1():
    while True:
        print("쓰레드1 동작")
        time.sleep(1.0)

t1 = threading.Thread(target=thread_1)
t1.start()

while True:
    print("메인동작")
    time.sleep(2.0)