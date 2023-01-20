# pywinauto 를 이용하여 메모장 실행

# pip install pywinauto
# 실행파일 만들기

from pywinauto import Application
import time

app = Application(backend="uia").start("notepad.exe")

dig = app.window(title_re=".* 메모장")

#최대화 버튼 클릭
dig['최대화Button'].click()

#문서작성
#dig['Document'].type_keys("안녕하세요{ENTER}SSS급 일잘러를 위한{ENTER}파이썬과 40개의 작품들 입니다.", with_spaces=True)
dig.Document.type_keys("안녕하세요{ENTER}SSS급 일잘러를 위한{ENTER}파이썬과 40개의 작품들 입니다.", with_spaces=True)
time.sleep(2.0)

#파일종료
dig.Pane1.menu_select("파일->종료")
dig2 = app['메모장Dialog']
dig2.저장하지않음.click()