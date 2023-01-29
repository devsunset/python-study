import smtplib
from email.mime.text import MIMEText
import pandas as pd
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

excel_file_path = '이름_점수_이메일.xlsx'
df_from_excel = pd.read_excel(excel_file_path)

name_list = df_from_excel['이름'].tolist()
score_list = df_from_excel['점수'].tolist()
email_list = df_from_excel['이메일'].tolist()

def send_naver_google_email(naver_or_google,send_email,send_pwd,recv_email,subject,text):
    try:
        if naver_or_google == "naver":
            smtp_name = "smtp.naver.com" 
            smtp_port = 587
        else:
            smtp_name = "smtp.gmail.com"
            smtp_port = 587

        msg = MIMEText(text)

        msg['Subject'] = subject
        msg['From'] = send_email
        msg['To'] = recv_email

        s=smtplib.SMTP( smtp_name , smtp_port )
        s.starttls()
        s.login( send_email , send_pwd )
        s.sendmail( send_email, recv_email, msg.as_string() )
        s.quit()
        return recv_email + " 메일을 성공적으로 보냈습니다."
    except:
        return recv_email + " 메일보내는데 실패하였습니다."

send_email = ""
send_pwd = ""

for i in range(len(name_list)):
    recv_email = email_list[i]
    subject = name_list[i] + " 님의 점수 결과입니다."
    text = name_list[i] + ' 님의 점수 는 ' + str(score_list[i]) + ' 점 입니다.'
    result = send_naver_google_email("naver",send_email,send_pwd,recv_email,subject,text)
    print(result)