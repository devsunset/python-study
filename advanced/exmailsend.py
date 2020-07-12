
# case 1 -  mail send

import smtplib
from email.mime.text import MIMEText

sendEmail = "sender email"
recvEmail = "receiver email"
password = "password"

# gmail
smtpName = "smtp.gmail.com" 
smtpPort = 587 

# naver
# smtpName = "smtp.naver.com" 
# smtpPort = 587

text = "mail content"
msg = MIMEText(text, _charset = "utf8") 
msg['Subject'] ="mail title"
msg['From'] = sendEmail
msg['To'] = recvEmail

print(msg.as_string())

s=smtplib.SMTP( smtpName , smtpPort )
s.starttls()
s.login( sendEmail , password ) 
s.sendmail( sendEmail, recvEmail, msg.as_string() ) 
s.close() 

# case 2 -  mail (with attachment file) send

import smtplib 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication 

sendEmail = "sender email"
recvEmail = "receiver email"
password = "password"

# gmail
smtpName = "smtp.gmail.com" 
smtpPort = 587 

# naver
# smtpName = "smtp.naver.com" 
# smtpPort = 587

msg = MIMEMultipart()
msg['Subject'] ="mail title"
msg['From'] = sendEmail
msg['To'] = recvEmail

text = "mail content"
contentPart = MIMEText(text , _charset = "utf8")
msg.attach(contentPart) 

etcFileName = 'file_name'
with open(etcFileName, 'rb') as etcFD : 
    etcPart = MIMEApplication( etcFD.read() )
    etcPart.add_header('Content-Disposition','attachment', filename=etcFileName)
    msg.attach(etcPart) 

s=smtplib.SMTP( smtpName , smtpPort )
s.starttls()
s.login( sendEmail , password ) 
s.sendmail( sendEmail, recvEmail, msg.as_string() )  
s.close() 


