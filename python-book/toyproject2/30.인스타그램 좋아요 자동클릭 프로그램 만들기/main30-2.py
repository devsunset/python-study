import pyautogui
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

pic_position = pyautogui.locateOnScreen("instar_pic.png", confidence=0.8) 
click_position = pyautogui.center(pic_position)

print(click_position)