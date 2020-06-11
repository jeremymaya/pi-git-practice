#!/usr/bin/env python3

import sys
import os
import emails
import re
from decouple import config

SENDER = config("SENDER")
RECIPIENT = config("RECIPIENT")

def check_temperature():
    measure_temp = os.popen("vcgencmd measure_temp").readline()
    temp = re.findall('\d*\.?\d+', measure_temp)
    return float(temp[0]) < 80.0

def send_alert(subject):
    sender = SENDER
    recipient = RECIPIENT
    body = emails.generate_alert_email(SENDER, RECIPIENT, subject, body)
    emails.send_email(message)

def main(argv):
    if not check_temperature():
        sibject = "Alert - The core temperature is over 80.0'C"
        send_alert(subject)

if __name__ == "__main__":
    main(sys.argv)
