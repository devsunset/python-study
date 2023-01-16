import tkinter
import tkinter.font
from tkinter import *
from tkinter import filedialog
import os
import threading
from rembg import remove


#변환 할 사진선택
def select_file_click():
    dir_path = filedialog.askopenfilename(parent=window,initialdir="\\",title='파일을 선택하세요')
    print(dir_path)
    start_path.config(text=dir_path)

#시작버튼이 클릭되면 이미지 배경제거 쓰레드 실행
def btn_go_click():
    threading.Thread(target=img_proc_thread).start()

#이미지 배경제거 쓰레드
def img_proc_thread():
    file_path = start_path.cget("text")
    lb_state.config(text="변환중 입니다....")
    output_path = os.path.dirname(file_path) + "\\변환완료_" + os.path.basename(file_path)
    with open(file_path, 'rb') as i:
        with open(output_path, 'wb') as o:
            input = i.read()
            output = remove(input)
            o.write(output)
    lb_state.config(text="변환 완료!!!")

#tkinter 윈도우설정
window=tkinter.Tk()
window.title("이미지배경제거")
window.geometry("380x80+800+300")
window.resizable(False, False)

#파일선택 버튼
start_path = Label(window,width=40,anchor="se")
start_path.grid(row=0, column=0)
btn_start = tkinter.Button(window, overrelief="solid",text="파일선택", width=10, command=select_file_click, repeatdelay=1000, repeatinterval=100)
btn_start.grid(row=0, column=1)

#실행버튼 생성
btn_go = tkinter.Button(window, overrelief="solid",text="실행", width=10, command=btn_go_click, repeatdelay=1000, repeatinterval=100)
btn_go.grid(row=3, column=0)

#마지막줄에 상태를 표시하는 라벨 생성
lb_state = Label(window,width=40,text="파일을 선택 후 실행버튼을 눌러 실행하세요")
lb_state.grid(row=4, column=0)

window.mainloop()