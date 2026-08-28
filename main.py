import os
import csv
import smtplib
from dotenv import load_dotenv
from email.message import EmailMessage

load_dotenv()

emailAddress = os.environ.get("GMAIL_USER")
emailPass = os.environ.get("GMAIL_PASSWORD")

file_path = "C:/Users/Yamkelo/Desktop/msp-outreach-automator/test.csv"

try:
    with open(file_path, "r") as file:
        content = csv.reader(file)
        row = list(content)
        recipient_name = (row[1][3])
        recipient_email = (row[1][1])

        msg = EmailMessage()
        msg["Subject"] = "Lets Gooo!"
        msg["From"] = emailAddress
        msg["To"] = recipient_email
        msg.set_content(f"Hi there {recipient_name}")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
     
        smtp.login(emailAddress, emailPass)

        smtp.send_message(msg)

except FileNotFoundError:
    print("The file was not found!")



