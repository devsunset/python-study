import smtplib
from email.mime.text import MIMEText

# 구굴 메일 보내기 (IMAP/SMTP 설정 필요)

send_email = "구글계정 메일주속"
send_pwd = "구글계정에서 앱비밀번호생성"

recv_email = "받는메일주소"

smtp_name = "smtp.gmail.com"
smtp_port = 587

text = """
메일 내용을 여기에 적습니다.
여러줄을 입력하여도 됩니다.
"""
msg = MIMEText(text)

msg['Subject'] ="메일제목은 여기에 넣습니다"
msg['From'] = send_email
msg['To'] = recv_email
print(msg.as_string())

s=smtplib.SMTP( smtp_name , smtp_port )
s.starttls()
s.login( send_email , send_pwd )
s.sendmail( send_email, recv_email, msg.as_string() )
s.quit()