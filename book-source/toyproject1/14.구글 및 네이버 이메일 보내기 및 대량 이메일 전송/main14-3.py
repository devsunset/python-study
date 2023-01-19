import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# 첨부 파일 포함 메일 보내기

send_email = "구글계정 메일주속"
send_pwd = "구글계정에서 앱비밀번호생성"

recv_email = "받는메일주소"

smtp_name = "smtp.gmail.com"
smtp_port = 587

msg = MIMEMultipart()

msg['Subject'] ="첨부파일 테스트 입니다."
msg['From'] = send_email 
msg['To'] = recv_email 

text = """
첨부파일 메일 테스트 내용 입니다.
감사합니다.
"""
contentPart = MIMEText(text) 
msg.attach(contentPart) 

etc_file_path = '첨부파일.txt'
with open(etc_file_path, 'rb') as f : 
    etc_part = MIMEApplication( f.read() )
    etc_part.add_header('Content-Disposition','attachment', filename="첨부파일.txt")
    msg.attach(etc_part)

s=smtplib.SMTP( smtp_name , smtp_port )
s.starttls()
s.login( send_email , send_pwd )
s.sendmail( send_email, recv_email, msg.as_string() )
s.quit()