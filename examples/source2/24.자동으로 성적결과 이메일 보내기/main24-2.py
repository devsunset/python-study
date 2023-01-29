import smtplib
from email.mime.text import MIMEText

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
        #print(msg.as_string())

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
recv_email = ""
subject = "메일 제목 입니다.22"
text = """ 메일 내용을 입력합니다.
여러줄 입력하여도 됩니다.
"""

print( send_naver_google_email("naver",send_email,send_pwd,recv_email,subject,text) )