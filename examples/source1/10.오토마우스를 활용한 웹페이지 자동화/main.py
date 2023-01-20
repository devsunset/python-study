import time
# pip install pyautogui
import pyautogui
# pip install pyperclip
import pyperclip

# 검색 엔진 에서 검색 후 결과를 캡쳐 하는 처리
# Mac 에서 테스트 시 정상 동작 하지 않음 검토 필요

# 마우스 좌표 출력
# while True:
#     print(pyautogui.position())
#     time.sleep(0.1)

print("=========================================")

pyautogui.moveTo(1266,234,0.2) # 검색어 입력 좌표
pyautogui.click()
time.sleep(0.5)

# 한글 입력의 경우 pyautogui.write 에서 처리가 안되기 때문에 pyperclip 를 사용
pyperclip.copy("파이썬")
pyautogui.hotkey("ctrl", "v")

# 값을 입력 처리 - 한글 지원 안됨
#pyautogui.write("python",interval=0.1)
time.sleep(0.5)

pyautogui.write(["enter"])
time.sleep(1)

# 좌표는 캡쳐 원하는 좌표 확인 하여 수정 필요
start_x = 992
start_y = 220
end_x = 1656
end_y = 635

# 화면 캡쳐 저장
pyautogui.screenshot('python.png', region=(start_x, start_y, end_x-start_x, end_y-start_y))
