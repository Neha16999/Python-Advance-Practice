import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path


html=Template(Path('index.html').read_text())
email=EmailMessage()
email['from']='Neha Rathi'
email['to']='neharathi1699@gmail.com'
email['subject']='You have to complete your dream through your Karma.'

email.set_content(html.substitute({'name' :'Neha'}),'html')

with smtplib.SMTP(host='smtp.gmail.com', port = 587) as smtp:
    smtp.ehlo()     #smtp hello
    smtp.starttls()     #tls is encryption mechanism
    smtp.login('neharathi16999@gmail.com', '9405150370')  #email and password
    smtp.send_message(email)
    print('All good Boss !')



