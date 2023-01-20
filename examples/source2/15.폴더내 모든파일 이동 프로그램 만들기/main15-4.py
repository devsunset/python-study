import tkinter
import tkinter.font
from tkinter import *
from tkinter import filedialog
import os
import threading
import time
import shutil

#폴더 선택 버튼을 클릭하면 동작
def bnt_select_click():
    dir_path = filedialog.askdirectory(parent=window,initialdir="\\",title='폴더를 선택하세요')
    print(dir_path)
    start_path.config(text=dir_path)

#실행버튼이 클릭되면
def btn_go_click():
    threading.Thread(target=move_thread).start()

#파일이동 쓰레드 동작
def move_thread():
    path = start_path.cget("text")
    lb_state.config(text="이동중...")
    for dirpath, dirname, files in os.walk(path):
        for filename in files:
            try:
                print(os.path.join(dirpath, filename))
                shutil.move(os.path.join(dirpath, filename), path)
            except:
                pass
    lb_state.config(text="이동완료...")
    time.sleep(5.0)
    lb_state.config(text="실행버튼을 눌러 이동하세요")

#tkinter 윈도우설정
window=tkinter.Tk()
window.title("파일이동")
window.geometry("650x80+800+300")
window.resizable(False, False)

#폴더 및 버튼
start_path = Label(window,width=80,anchor="se")
start_path.grid(row=0, column=0)
btn_start = tkinter.Button(window, overrelief="solid",text="폴더선택", width=10, command=bnt_select_click, repeatdelay=1000, repeatinterval=100)
btn_start.grid(row=0, column=1)

#실행버튼 생성
btn_go = tkinter.Button(window, overrelief="solid",text="실행", width=10, command=btn_go_click, repeatdelay=1000, repeatinterval=100)
btn_go.grid(row=3, column=0)

#마지막줄에 상태를 표시하는 라벨 생성
lb_state = Label(window,width=40,text="실행버튼을 눌러 이동하세요")
lb_state.grid(row=4, column=0)

window.mainloop()