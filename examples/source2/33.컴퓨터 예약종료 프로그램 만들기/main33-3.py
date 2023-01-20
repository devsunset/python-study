import tkinter
from tkinter import *
import tkinter.ttk
import os

#실행 버튼 누르면 동작하는 함수
def btn_action():
    os.system('shutdown -a') 
    hour = int(time_combobox.get().split("시간")[0])
    min = int(min_combobox.get().split("분")[0])
    set_time = str((hour * 3600) + (min * 60))
    os.system(f'shutdown -s -t {set_time}') 

#취소버튼 누르면 동작하는 함수
def btn_cancer():
    os.system('shutdown -a') 

window=tkinter.Tk()
window.title("컴퓨터 전원끄기")
window.geometry("200x150+600+200")
window.resizable(False, False)

lb_huor = Label(window,width=10,text="시간:")
lb_huor.grid(row=0, column=0)

time_values=[str(i)+"시간" for i in range(0, 24)] 
time_combobox=tkinter.ttk.Combobox(window, width=10, height=10, values=time_values)
time_combobox.grid(row=0, column=1,pady=5)
time_combobox.set(time_values[0])

lb_min = Label(window,width=10,text="  분:")
lb_min.grid(row=1, column=0)

min_values=[str(i)+"분" for i in range(0, 60)] 
min_combobox=tkinter.ttk.Combobox(window, width=10, height=10, values=min_values)
min_combobox.grid(row=1, column=1,pady=5)
min_combobox.set(min_values[30])

#실행
btn_action = tkinter.Button(window, overrelief="solid",text="실행", width=10, 
                          command=btn_action, repeatdelay=1000, repeatinterval=100)
btn_action.grid(sticky = N + E + S + W,row=4,columnspan=3,padx=10,pady=5)

#취소
btn_cancer = tkinter.Button(window, overrelief="solid",text="취소", width=10, 
                          command=btn_cancer, repeatdelay=1000, repeatinterval=100)
btn_cancer.grid(sticky = N + E + S + W,row=5,columnspan=3,padx=10,pady=5)

window.mainloop()