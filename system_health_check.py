#!/usr/bin/env python3

import sys
import os
import shutil
import psutil
import emails
import re
from decouple import config

SENDER = config("SENDER")
RECIPIENT = config("RECIPIENT")

def check_temperature():
    measure_temp = os.popen("vcgencmd measure_temp").readline()
    temp = re.findall(r'\d*\.?\d+', measure_temp)
    return float(temp[0]) < 80.0

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(1)
    return cpu_usage < 80

def check_memory_usage():
    memoery_usage = psutil.virtual_memory().available
    used = memoery_usage / (1024.0 ** 2)
    return used > 500

def check_disk_usage(disk):
    disk_usage = shutil.disk_usage(disk)
    free = disk_usage.free / disk_usage.total * 100
    return free > 20

def send_alert(subject):
    body = "Check the system and resolve the issue"
    message = emails.generate_alert_email(SENDER, RECIPIENT, subject, body)
    emails.send_email(message)

def main(argv):
    if not check_temperature():
        subject = "Alert - Core temperature is over 80.0'C"
        send_alert(subject)
    if not check_cpu_usage() :
        subject="Alert - CPU usage is over 80%"
        send_alert(subject)
    if not check_memory_usage():
        subject = "Alert - Available memory is less than 500MB"
        send_alert(subject)
    if not check_disk_usage('/') :
        subject = "Alert - Available disk space is less than 20%"
        send_alert(subject)

if __name__ == "__main__":
    main(sys.argv)
