import os
import csv
import time
import random
import smtplib
from dotenv import load_dotenv
from email.message import EmailMessage

load_dotenv()

emailAddress = os.environ.get("GMAIL_USER")
emailPass = os.environ.get("GMAIL_PASSWORD")

N_message_file_path = "N_message.txt"
S_message_file_path = "S_message.txt"
recipients_file_path = "targets.csv"

try:
    with open(N_message_file_path, "r") as N_message:
         N_text = N_message.read()

    with open(S_message_file_path, "r") as S_message:
         S_text = S_message.read()

    with open(recipients_file_path, "r") as file:
        content = csv.reader(file)
        rows = list(content)

    with open("N_resume.pdf", "rb") as f:
         N_resume_data = f.read()
         N_resume_name = f.name

    with open("S_resume.pdf", "rb") as f:
         S_resume_data = f.read()
         S_resume_name = f.name

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
         smtp.login(emailAddress, emailPass)

         for row in rows[1:]:
            recipient_name = row[3]
            recipient_email = row[1]
            position_type = row[4].strip().upper()

            if position_type == "N":
               text = N_text
               resume_data = N_resume_data
               resume_name = N_resume_name

            elif position_type == "S":
                 text = S_text
                 resume_data = S_resume_data
                 resume_name = S_resume_name

            else:
                 text = N_text
                 resume_data = N_resume_data
                 resume_name = N_resume_name
                              
            msg = EmailMessage()
            msg["Subject"] = "Lets Gooo!"
            msg["From"] = emailAddress
            msg["To"] = recipient_email
            msg.set_content(f"Hi {recipient_name}\n{text}")

            msg.add_attachment(
                resume_data, 
                maintype="application", 
                subtype="pdf", 
                filename=resume_name
                )

            smtp.send_message(msg)
            print(f"emails was sent to {recipient_name}")
            delay_time = int(random.uniform(5, 10))
            print(f"waiting {delay_time} seconds before sending the next email...")
            time.sleep(delay_time)


except FileNotFoundError:
       print("The file was not found!")



