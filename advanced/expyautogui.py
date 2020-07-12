# $ pip install pyautogui
# $ pip install opencv-python

import pyautogui
import time

# Get Mouse position
print(pyautogui.position()) 

# Move Mouse position
pyautogui.moveTo(150,200)
pyautogui.moveTo(300,300,2)
pyautogui.moveRel(0,300,2)

# Mouse Click
pyautogui.click()
pyautogui.click(100,100)
pyautogui.click(clicks=2,interval=2)
pyautogui.doubleClick()

# keyboard write
# notepad open ex) notepad icon positon 100,100
pyautogui.moveTo(100,100)
pyautogui.doubleClick()
time.sleep(3) # program open wait time
pyautogui.typewrite(['enter']) # [ ] keyboard key press
pyautogui.typewrite('Hello World') # keyboard text write

# Get Image position 
p = pyautogui.locateOnScreen('test.png')
print(p)
c = pyautogui.center(p)
pyautogui.click(c)

c = pyautogui.locateCenterOnScreen('test.png')
pyautogui.click(c)

# Get Screen Capture Image position 
print(pyautogui.position()) 
pyautogui.screenshot('test_capture.png', region=(1200,1000,30,30))
c = pyautogui.locateCenterOnScreen('test_capture.png')
pyautogui.click(c)