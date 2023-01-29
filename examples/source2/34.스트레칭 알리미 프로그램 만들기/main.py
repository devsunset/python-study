import tkinter
import tkinter.font
from tkinter import *
import tkinter.ttk
import threading
import time
from playsound import playsound
from gtts import gTTS
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# text = "스트레칭 시간입니다. 자리에서 일어나 스트레칭 하세요"
# tts = gTTS(text=text, lang='ko')
# tts.save("tts.mp3")
# playsound("tts.mp3")

is_on = False
set_time = 0

#실행 버튼 누르면 동작하는 함수
def btn_action():
    global is_on
    global set_time
    if btn_action.config('text')[-1] == '실행':
        btn_action.config(text='종료')
        hour = int(time_combobox.get().split("시간")[0])
        min = int(min_combobox.get().split("분")[0])
        set_time = (hour * 3600) + (min * 60)
        is_on = True
        print("실행")
    else:
        btn_action.config(text='실행')
        is_on = False
        print("종료")

window = tkinter.Tk()
window.title("스트레칭 알리미")
window.geometry("250x150+600+200")
window.resizable(False,False)

time_values=[str(i)+"시간" for i in range(0, 24)] 
time_combobox=tkinter.ttk.Combobox(window, width=5, height=5, values=time_values)
time_combobox.grid(row=0, column=0,padx=3)
time_combobox.set(time_values[0])

lb1 = Label(window,width=1,text=":")
lb1.grid(row=0, column=1)

min_values=[str(i)+"분" for i in range(0, 60)] 
min_combobox=tkinter.ttk.Combobox(window, width=5, height=5, values=min_values)
min_combobox.grid(row=0, column=2,padx=3)
min_combobox.set(min_values[30])

lb2 = Label(window,width=5,text="후에")
lb2.grid(row=0, column=3)

lb3 = Label(window,width=30,text="스트레칭 알림이 동작합니다.")
lb3.grid(row=1, column=0 ,columnspan=4,pady=5)

#실행
btn_action = tkinter.Button(window, overrelief="solid",text="실행", width=10, 
                          command=btn_action, repeatdelay=1000, repeatinterval=100)
btn_action.grid(sticky = N + E + S + W,row=2,column=1,columnspan=2,padx=5,pady=5)

font = tkinter.font.Font(size = 30)
label=tkinter.Label(window, text="남은시간", font=font)
label.grid(row=3, column=0 ,columnspan=4,pady=5)


def play_sound():
    global is_on
    while True:
        playsound("tts.mp3")
        if is_on == False:
            break

def timer_1sec():
    global is_on
    global set_time
    window.after(1000,timer_1sec)
    if is_on == True:
        label.config(text=str(set_time))
        if set_time > 0:
            set_time = int(set_time) - 1
        if set_time == 0:
            t1 = threading.Thread(target=play_sound)
            t1.daemon = True
            t1.start()
            set_time = -1

timer_1sec()
window.mainloop()