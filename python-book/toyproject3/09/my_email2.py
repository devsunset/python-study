﻿from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP_SSL

SMTP_SERVER = 'smtp.naver.com'
SMTP_PORT=465
SMTP_USER = 'lthlovelee'
# 실제 비밀번호를 입력해야 합니다.
SMTP_PASSWORD = ''

def send_mail(name, recvs, cc, hidden_cc, contents, attachment=False):
    msg = MIMEMultipart('alternative')

    if attachment:
        msg = MIMEMultipart('mixed')

    msg['From'] = SMTP_USER + '@naver.com'
    msg['To'] = recvs
    msg['CC'] = cc
    msg['Subject'] = name+'님, 메일이 도착했습니다.'

    text = MIMEText(contents)
    msg.attach(text)

    if attachment:
        from email.mime.base import MIMEBase
        from email import encoders

        file_data = MIMEBase('application', 'octet-stream')
        f = open(attachment,'rb')
        file_contents = f.read()
        file_data.set_payload(file_contents)
        encoders.encode_base64(file_data)

        from os.path import basename
        filename = basename(attachment)
        file_data.add_header('Content-Disposition', 'attachment', filename=filename)
        msg.attach(file_data)

    targets = ','.join((recvs, cc, hidden_cc))

    smtp = SMTP_SSL(SMTP_SERVER, SMTP_PORT)
    smtp.login(SMTP_USER, SMTP_PASSWORD)
    smtp.sendmail('......@naver.com', targets.split(','), msg.as_string())
    smtp.close()

send_mail('이태화', '.....@gmail.com,......@lahion.com',
        '......@naver.com', 'alghost@moreum.co.kr', '테스트입니다')


