from email.message import EmailMessage
from app2 import password
import ssl
import smtplib

email_sender='praneet.gogoi@gmail.com'
email_password=password
email_reciever=''

subject="Welcome fellas! To the world of coding with praneet"
body="""
this is the test email send out by my python code
"""

em=EmailMessage()
em['From']=email_sender
em['to']=email_reciever
em['subject']=subject
em.set_content(body)


context=ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_reciever,em.as_string())