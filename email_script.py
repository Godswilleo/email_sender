import smtplib
import ssl


smtp_server = 'smtp.gmail.com'
port = 465

sender_email = 'senders-email@gmail.com'
password = 'email-password'

recipient_email = ['email-address1@xyz.com', 'email-address2@xyz.com']


message = '''\
From: Sender's name <senders-email@gmail.com>
Subject: Test Subject

This will contain the body of the email
'''

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, recipient_email, message)
 