import pyautogui
import time
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#인스타 그램 아이콘 클릭
try:
    pic_position = pyautogui.locateOnScreen("instar_pic.png", confidence=0.8) 
    click_position = pyautogui.center(pic_position)
    pyautogui.click(click_position)
    time.sleep(1.0)
except:
    print("인스타 아이콘 클릭 실패")


#좋아요 자동 클릭
for i in range(50):
    #스크롤을 아래로 내림
    pyautogui.scroll(-700)
    time.sleep(1.0)
    try:
        pic_position = pyautogui.locateOnScreen("like.png", confidence=0.9, region=(1300,300, 600, 700)) 
        click_position = pyautogui.center(pic_position)
        time.sleep(0.5)
        pyautogui.click(click_position)
        print("좋아요 클릭")
        time.sleep(1.0)
    except:
        print("좋아요 아이콘을 찾지 못했습니다.")