import pyautogui
import pyperclip
import time
import schedule
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def click_mac():
    picPosition = pyautogui.locateOnScreen('mac.png')
    print(picPosition)

    clickPosition = pyautogui.center(picPosition)
    pyautogui.click(clickPosition)

    # pyperclip.copy("hello")
    # pyautogui.hotkey("ctrl", "v")
    # time.sleep(1.0)

    # pyautogui.write(["enter"])
    # time.sleep(1.0)

    time.sleep(3.0)
    pyautogui.write(["escape"])


schedule.every(10).seconds.do(click_mac)

while True:
    schedule.run_pending()
    time.sleep(1)