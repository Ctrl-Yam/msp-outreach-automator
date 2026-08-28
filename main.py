import os
import smtplib
from dotenv import load_dotenv
from email.message import EmailMessage

load_dotenv()

emailAddress = os.environ.get("GMAIL_USER")
emailPass = os.environ.get("GMAIL_PASSWORD")
to_emailAddress = os.environ.get("DESTINATION_EMAIL")

msg = EmailMessage()
msg["Subject"] = "Lets Gooo!"
msg["From"] = emailAddress
msg["To"] = to_emailAddress
msg.set_content("We just won the speedrun")

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
     smtp.login(emailAddress, emailPass)

     smtp.send_message(msg)