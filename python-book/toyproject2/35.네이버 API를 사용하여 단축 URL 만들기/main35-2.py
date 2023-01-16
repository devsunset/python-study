import tkinter
from tkinter import *

def btn_shorturl_click():
    print("버튼 클릭")

#tkinter 윈도우설정
window=tkinter.Tk()
window.title("단축 URL")
window.geometry("320x80+800+300")
window.resizable(False, False)

#라벨
lb1_text = Label(window,width=10,text="url입력:")
lb1_text.grid(row=0, column=0)

#URL 입력
entry_password = Entry(window,width=20)
entry_password.grid(row=0, column=1,pady=10)

#실행버튼
btn_ok = tkinter.Button(window, overrelief="solid",text="실행", width=5, 
                        command=btn_shorturl_click, repeatdelay=1000, repeatinterval=100)
btn_ok.grid(row=0, column=2,padx=5)

#라벨
lb2_text = Label(window,width=10,text="결과:")
lb2_text.grid(row=1, column=0)

#URL 결과
entry_result = Entry(window,width=28)
entry_result.grid(row=1, column=1, columnspan=2,pady=5)

# tkinter 메인루프 실행
window.mainloop()