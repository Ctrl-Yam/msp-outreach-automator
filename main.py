import os
import csv
import smtplib
from dotenv import load_dotenv
from email.message import EmailMessage

load_dotenv()

emailAddress = os.environ.get("GMAIL_USER")
emailPass = os.environ.get("GMAIL_PASSWORD")

file_path = "targets.csv"

try:
    with open(file_path, "r") as file:
        content = csv.reader(file)
        rows = list(content)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
         smtp.login(emailAddress, emailPass)

         for row in rows[1:]:
            recipient_name = row[3]
            recipient_email = row[1]
            print(f"emails was sent to {recipient_name}")

            with open("resume.pdf", "rb") as f:
                 resume_data = f.read()
                 resume_name = f.name

            msg = EmailMessage()
            msg["Subject"] = "Lets Gooo!"
            msg["From"] = emailAddress
            msg["To"] = recipient_email
            msg.set_content(f"Hi there {recipient_name}")

            msg.add_attachment(
                resume_data, 
                maintype="application", 
                subtype="pdf", 
                filename=resume_name
                )

            smtp.send_message(msg)

except FileNotFoundError:
    print("The file was not found!")



