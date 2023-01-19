import tkinter
from tkinter import *
import cryptocode

#암호화 버튼 클릭시 동작하는 함수
def btn_encrypt_click():
    print("암호화 버튼 클릭")

#복호화 버튼 클릭시 동작하는 함수
def btn_decrypt_click():
    print("복호화 버튼 클릭")

#tkinter 윈도우설정
window=tkinter.Tk()
window.title("암호화 및 복호화")
window.geometry("320x400+800+300")
window.resizable(False, False)

#글자표시
lb_text = Label(window,width=10,text="비밀번호:")
lb_text.grid(row=0, column=0)

#비밀번호 입력
entry_password = Entry(window,width=20,show='*')
entry_password.grid(row=0, column=1)

#암호화 버튼
btn_ok = tkinter.Button(window, overrelief="solid",text="암호화", width=5, 
                        command=btn_encrypt_click, repeatdelay=1000, repeatinterval=100)
btn_ok.grid(row=0, column=2,padx=5)

#복호화 버튼
btn_save = tkinter.Button(window, overrelief="solid",text="복호화", width=5, 
                          command=btn_decrypt_click, repeatdelay=1000, repeatinterval=100)
btn_save.grid(row=0, column=3,padx=5)

#텍스트구역
text_area = Text(window)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
text_area.grid(sticky = N + E + S + W,row=2,columnspan=4,padx=10,pady=10)

# tkinter 메인루프 실행
window.mainloop()