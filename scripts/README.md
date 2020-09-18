# Scripts

Author: Kyungrae Kim

----

## Monitoring Raspberry Pi OS

Proactive monitoring of the system is crucial for ensuring uptime. Critical system components will be monitored using the following scripts with ```cron``` which is scheduled to run ```system_health_check.py``` every hour.

* ```emails.py```
* ```system_health_check.py```

### Core Temperature

Core temperature is monitored using ```check_temperature``` method. If the core temperature rises above 80.0'C, the method sends an alert email.

### CPU Usage

CPU usage is monitored using ```check_cpu_usage``` method. If the CPU usage is over 80%, the method sends an alert email.

### Memory Usage

Memory usage is monitored using ```check_memoery_usage``` method. If the available memory is less than 500MB, the method sends an alert email.

### Disk Usage

Disk usage is monitored using ```check_disk_usage``` method. If the available memory is less than 20%, the method sends an alert email.

----

## Credits

* [Raspberry Pi Foundation - Getting started with Git](https://projects.raspberrypi.org/en/projects/getting-started-with-git)
* [Able@rhett - How to Set and Get Environment Variables in Python](https://able.bio/rhett/how-to-set-and-get-environment-variables-in-python--274rgt5)
* [Medium@kevalpatel2106 - Monitor the core temperature of your Raspberry Pi](https://medium.com/@kevalpatel2106/monitor-the-core-temperature-of-your-raspberry-pi-3ddfdf82989f)
* [tutorialspoint - Extract decimal numbers from a string in Python](https://www.tutorialspoint.com/Extract-decimal-numbers-from-a-string-in-Python)
* [Maker Portal - Using Raspberry Pi and Python to Send Email Alerts](https://makersportal.com/blog/2017/9/23/using-raspberry-pi-and-python-to-send-email-alerts)
* [Admin's Choise - Crontab](https://www.adminschoice.com/crontab-quick-reference)

## Change Log

* *Initial setup* - 11 June 2020
