# pip install pure-python-adb
# adb 설치
# platform-tools/ ./adb start-server
# https://developer.android.com/reference/android/view/KeyEvent

from ppadb.client import Client
import time

def adb_connect():
    client = Client(host="127.0.0.1", port=5037) 
    find_devices = client.devices()

    if len(find_devices) == 0:
        print('No devices')
        quit()

    device = find_devices[0]
    print(f'찾은 디바이스: {device}')

    return device, client

device, client = adb_connect()

device.shell('input keyevent 64')
time.sleep(2.0)

xyPosition = "423 136"
device.shell(f'input tap {xyPosition}')
time.sleep(2.0)

url = "www.naver.com"
device.shell(f'input text {url}')
time.sleep(2.0)

device.shell('input keyevent 66')
time.sleep(2.0)

result = device.screencap()
with open("screen.png", "wb") as fp:
    fp.write(result)