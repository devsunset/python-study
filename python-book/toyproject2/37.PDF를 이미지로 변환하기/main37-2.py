import tkinter
import tkinter.font
from tkinter import *
from tkinter import filedialog
import os
from pdf2image import convert_from_path

#파일선택
def file_select_bnt_click():
    file_path = filedialog.askopenfilename(parent=window,initialdir="\\",title='PDF 파일을 선택하세요')
    print(file_path)
    lb_file_path.config(text=file_path)

#실행버튼 클릭시 변환
def btn_go_click():
    pdf_path = lb_file_path.cget("text")
    pdf_name = os.path.basename(pdf_path)
    pdf_dir = os.path.dirname(pdf_path)
    
    poppler_bin_path = r"C:\일잘러 파이썬과 40개의 작품들 코드\37.PDF를 이미지로 변환하기\poppler-0.68.0\bin"
    images = convert_from_path(pdf_path, poppler_path= poppler_bin_path)

    for i, image in enumerate(images):
        image.save(pdf_dir + '\\' + pdf_name.split('.')[0]+str(i)+".jpg", "JPEG")

#tkinter 윈도우설정
window=tkinter.Tk()
window.title("PDF 이미지 변환")
window.geometry("600x80+800+300")
window.resizable(False, False)

#파일 경로
lb_file_path = Label(window,width=75,anchor="n",text="파일을 선택하세요")
lb_file_path.grid(row=0, column=0)

#파일선택버튼 생성
btn_select = tkinter.Button(window, overrelief="solid",text="파일선택", width=8, command=file_select_bnt_click, repeatdelay=1000, repeatinterval=100)
btn_select.grid(row=0, column=1)

#실행버튼 생성
btn_go = tkinter.Button(window, overrelief="solid",text="변환", width=8, command=btn_go_click, repeatdelay=1000, repeatinterval=100)
btn_go.grid(row=1, column=0)

window.mainloop()