import imaplib
import email
from email import policy 
import requests
import json
import time

slack_webhook_url = "https://hooks.slack.com/services/..."

def sendSlackWebhook(strText):
    headers = {
    "Content-type": "application/json"
    }

    data = {
        "text" : strText
    }

    res = requests.post(slack_webhook_url, headers=headers, data=json.dumps(data))
    
    if res.status_code == 200:
        return "ok"
    else:
        return "error"

def find_encoding_info(txt):    
    info = email.header.decode_header(txt)
    subject, encode = info[0]
    return subject, encode

imap = imaplib.IMAP4_SSL('imap.naver.com')
id = '아이디'
pw = '비밀번호'
imap.login(id, pw)

send_list = []

while True:
    try:
        imap.select('INBOX')
        resp, data = imap.uid('search', None, 'All')
        all_email = data[0].split()
        last_email = all_email[-5:] 

        for mail in reversed(last_email):
            result, data = imap.uid('fetch', mail, '(RFC822)')
            raw_email = data[0][1]
            email_message = email.message_from_bytes(raw_email, policy=policy.default) 

            email_from = str(email_message['From'])
            email_date = str(email_message['Date'])
            subject, encode = find_encoding_info(email_message['Subject'])
            subject_str = str(subject)

            # print('=' * 70)
            # print('FROM:', email_message['From'])
            # print('SENDER:', email_message['Sender'])
            # print('TO:', email_message['To'])
            # print('DATE:', email_message['Date'])
            # subject, encode = find_encoding_info(email_message['Subject'])
            # print('SUBJECT:', subject)
            #
            # print('[CONTENT]')
            # message = ''
            # if email_message.is_multipart():
            #     for part in email_message.get_payload():
            #         if part.get_content_type() == 'text/plain':
            #             bytes = part.get_payload(decode=True)
            #             encode = part.get_content_charset()
            #             message = message + str(bytes, encode)
            # print(message)
            # print('=' * 70)
            
            if subject_str.find("정산") >= 0:
                slack_send_message =  email_from + '\n' + email_date + '\n' + subject_str
                if slack_send_message not in send_list:
                    sendSlackWebhook(slack_send_message)
                    print(slack_send_message)
                    send_list.append(slack_send_message)

        time.sleep(30)
    except KeyboardInterrupt:
        break

imap.close()
imap.logout()