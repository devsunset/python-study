import imaplib
import email
from email import policy 
import time
from win10toast import ToastNotifier
toaster = ToastNotifier()

imap = imaplib.IMAP4_SSL('imap.naver.com')
id = 'munjjac'
pw = 'mini0414~!@'
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
            subject_str = str(email_message['Subject'])
            print("메일 검사")
            if subject_str.find("입금") >= 0:
                if subject_str not in send_list:
                    send_list.append(subject_str)
                    toaster.show_toast("중요 메일이 도착하였습니다.",subject_str,duration=10)

        time.sleep(10)
    except KeyboardInterrupt:
        break

imap.close()
imap.logout()