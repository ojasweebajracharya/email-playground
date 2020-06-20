import smtplib

from email.message import EmailMessage

def sendEmail(sender, emailTo, emailSubject, emailContent, outlookEmail, outlookPassword):

    email = EmailMessage()

    email["from"] = sender
    email["to"] = emailTo
    email["subject"] = emailSubject

    email.set_content(emailContent)

    with smtplib.SMTP(host="smtp.outlook.com", port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(outlookEmail, outlookPassword)
        smtp.send_message(email)
        print("Its all good :D")

sender = input("From: ")
emailTo = input("Email to: ")
emailSubject = input("Subjet: ")
emailContent = input("Content of the email: ")

outlookEmail = input("Enter your outlook email: ")
outlookPassword = input("Enter your outlook password: ")

sendEmail(sender, emailTo, emailSubject, emailContent, outlookEmail, outlookPassword)
