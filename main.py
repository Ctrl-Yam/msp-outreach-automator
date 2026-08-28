import os
import smtplib
from dotenv import load_dotenv

load_dotenv()

emailAddress = os.environ.get('GMAIL_USER')
emailPass = os.environ.get('GMAIL_PASSWORD')


with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
     smtp.ehlo()
     smtp.starttls()
     smtp.ehlo()

     smtp.login(emailAddress, emailPass)

     subject = "FUUUCK!"
     body = "How about we go for a long walk?"

     msg = f"Subject: {subject} \n\n{body}"

     smtp.sendmail(emailAddress, "destination@gmail.com", msg)