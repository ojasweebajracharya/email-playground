import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path # similar to os.path

def sendEmail(sender, emailTo, emailSubject, outlookPassword):
    html = Template(Path("index.html").read_text())
    email = EmailMessage()

    email["from"] = sender
    email["to"] = emailTo
    email["subject"] = emailSubject

    email.set_content(html.substitute({"name":"Ojaswee"}), 'html')

    with smtplib.SMTP(host="smtp.outlook.com", port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(sender, outlookPassword)
        smtp.send_message(email)
        print("Its all good :D")

sender = input("From: ")
outlookPassword = input("Enter your outlook password: ")

emailTo = input("Email to: ")
emailSubject = input("Subject: ")


sendEmail(sender, emailTo, emailSubject, outlookPassword)
