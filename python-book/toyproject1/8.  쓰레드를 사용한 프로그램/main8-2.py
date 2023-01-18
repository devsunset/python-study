import threading
import time

# 메인코드가 동작할 때에만 쓰레드 동작
def thread_1():
    while True:
        print("쓰레드1 동작")
        time.sleep(1.0)

t1 = threading.Thread(target=thread_1)
t1.daemon = True
t1.start()

while True:
    print("메인동작")
    time.sleep(2.0)