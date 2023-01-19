import tkinter
from tkinter import *
import urllib.request
import json

def get_naver_shorturl(long_url,id,secret):
    encText = urllib.parse.quote(long_url)
    data = "url=" + encText
    url = "https://openapi.naver.com/v1/util/shorturl"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",id)
    request.add_header("X-Naver-Client-Secret",secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        response_json = json.loads(response_body.decode('utf-8'))
        return response_json['result']['url']
    else:
        return "Error Code:" + rescode

def btn_shorturl_click():
    client_id = "a0XLmXSasINGWGdq3D8b" 
    client_secret = "kRL4Ulaxhr"
    my_url = entry_url.get()
    short_url = get_naver_shorturl(my_url,client_id,client_secret)
    entry_result.delete(0,"end") 
    entry_result.insert(0,short_url)
    
#tkinter 윈도우설정
window=tkinter.Tk()
window.title("단축 URL")
window.geometry("320x80+800+300")
window.resizable(False, False)

#라벨
lb1_text = Label(window,width=10,text="url입력:")
lb1_text.grid(row=0, column=0)

#URL 입력
entry_url = Entry(window,width=20)
entry_url.grid(row=0, column=1,pady=10)

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