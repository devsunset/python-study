import imaplib
import email
from email import policy 

imap = imaplib.IMAP4_SSL('imap.naver.com')
id = 'munjjac'
pw = 'mini0414~!@'
imap.login(id, pw)

imap.select('INBOX')
resp, data = imap.uid('search', None, 'All')
all_email = data[0].split()
last_email = all_email[-10:] 

for mail in reversed(last_email):
    result, data = imap.uid('fetch', mail, '(RFC822)')
    raw_email = data[0][1]
    email_message = email.message_from_bytes(raw_email, policy=policy.default) 

    print('='*70)
    print('FROM:', email_message['From'])
    print('SENDER:', email_message['Sender'])
    print('TO:', email_message['To'])
    print('DATE:', email_message['Date'])
    print('SUBJECT:', email_message['Subject'])

imap.close()
imap.logout()