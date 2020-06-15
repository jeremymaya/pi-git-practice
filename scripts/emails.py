#!/usr/bin/env python3

import sys
import email
import smtplib
from decouple import config

SERVER = config("SMTP_SERVER")
PORT = config("SMTP_PORT")
USERNAME = config("USERNAME")
PASSWORD = config("PASSWORD")

def generate_alert_email(sender, recipient, subject, body):
    message = email.message.EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)

    return message

def send_email(message):
    mail_server = smtplib.SMTP_SSL(SERVER, port=PORT)
    mail_server.login(USERNAME, PASSWORD)
    mail_server.send_message(message)
    mail_server.quit()
