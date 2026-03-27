import smtplib
import os
from email.message import EmailMessage
from dotenv import load_dotenv
load_dotenv() # helps brigde the .env to the script

print(os.getenv("EMAIL_ID")) # create a .env file and store email id
print(os.getenv("PASSWORD"))
def send_email(subject, content, to_email):
	# EMAIL CONFIGURATION MAIL GOES HERE
	your_email = os.getenv("EMAIL_ID")
	your_password = os.getenv("PASSWORD")

	msg = EmailMessage()
	msg.set_content(content)
	msg["Subject"] = subject
	msg["From"] = your_email
	msg["To"] = to_email

	server = smtplib.SMTP("smtp.gmail.com",587)
	server.starttls()
	server.login(your_email,your_password)
	server.send_message(msg)
	server.quit()

send_email("Hello From Other Side", "Don't forget to like and subscribe!!","dipak.poudel077@gmail.com")

