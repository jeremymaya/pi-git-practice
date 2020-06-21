# Raspberry Pi OS

Author: Kyungrae Kim

This is a repository created from Raspberry Pi OS. I will be using this repository to become more familiar with Linux.

---

## Using Raspberry Pi OS Headless

### Remote Access

Raspberry Pi OS can be accessed remotely using [SSH (Secure Shell)](https://www.raspberrypi.org/documentation/remote-access/ssh/README.md), which allows user to access the command line of a Raspberry Pi remotely from another computer or device on the same network.

Refer to [Setting up a Raspberry Pi headless](https://www.raspberrypi.org/documentation/configuration/wireless/headless.md) in order to set up the Pi OS without a monitor or keyboard.

### Remote Development using SSH

Instead of using ```nano``` or other CLI based editors, [Visual Studio Code Remote - SSH extension](https://code.visualstudio.com/docs/remote/ssh) allows users to open a remote folder on any remote machine, virtual machine, or container with a running SSH server and take full advantage of VS Code's feature set.

---

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

---

## Turn on Wake on Lan enabled computers with Google Home

### Server

### WoL

---

## Configuration Management with Puppet

---

## Credits

* [Raspberry Pi Foundation - Getting started with Git](https://projects.raspberrypi.org/en/projects/getting-started-with-git)
* [Able@rhett - How to Set and Get Environment Variables in Python](https://able.bio/rhett/how-to-set-and-get-environment-variables-in-python--274rgt5)
* [Medium@kevalpatel2106 - Monitor the core temperature of your Raspberry Pi](https://medium.com/@kevalpatel2106/monitor-the-core-temperature-of-your-raspberry-pi-3ddfdf82989f)
* [tutorialspoint - Extract decimal numbers from a string in Python](https://www.tutorialspoint.com/Extract-decimal-numbers-from-a-string-in-Python)
* [Maker Portal - Using Raspberry Pi and Python to Send Email Alerts](https://makersportal.com/blog/2017/9/23/using-raspberry-pi-and-python-to-send-email-alerts)
* [Admin's Choise - Crontab](https://www.adminschoice.com/crontab-quick-reference)
* [Reddit - [GUIDE] Switch your PC from anywhere in the world with an OK Google command (using a RaspberryPi and wake on LAN)](https://www.reddit.com/r/googlehome/comments/didz91/guide_switch_your_pc_from_anywhere_in_the_world/)
* [Quora - What are the pros and cons of Node.js versus Apache web server?](https://www.quora.com/What-are-the-pros-and-cons-of-Node-js-versus-Apache-web-server)
* [How to Host a Raspberry Pi Web Server on the Internet with ngrok](https://thisdavej.com/how-to-host-a-raspberry-pi-web-server-on-the-internet-with-ngrok/)
* [intrinsic - Why should I use a Reverse Proxy if Node.js is Production-Ready?](https://medium.com/intrinsic/why-should-i-use-a-reverse-proxy-if-node-js-is-production-ready-5a079408b2ca)
* [How to Build a Raspberry Pi Server for Development](https://www.toptal.com/raspberry-pi/how-to-turn-your-raspberry-pi-into-a-development-server)
* [How do you set up a local testing server?](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/set_up_a_local_testing_server)
* [Python's http.server library “basic security checks”](https://security.stackexchange.com/questions/226095/pythons-http-server-library-basic-security-checks)
* [Dev - Run your Node.js application on a headless Raspberry Pi](https://dev.to/bogdaaamn/run-your-nodejs-application-on-a-headless-raspberry-pi-4jnn)
* [How to Run a Python script from Node.js](https://medium.com/swlh/run-python-script-from-node-js-and-send-data-to-browser-15677fcf199f)
* [Wake On LAN Python Script](https://dev.to/kevinmel2000/wake-on-lan-python-scrip-pf1)
* [WAKE ON LAN (PYTHON RECIPE)](http://code.activestate.com/recipes/358449-wake-on-lan/)
* [https://andreashessblog.wordpress.com/2016/12/10/python-script-wake-on-lan/](https://andreashessblog.wordpress.com/2016/12/10/python-script-wake-on-lan/)
* [Github - Python Wake on LAN](https://gist.github.com/rschuetzler/8854764)
* [Call Python script from bash with argument](https://stackoverflow.com/questions/14155669/call-python-script-from-bash-with-argument)
* [Configuration Management on Raspberry Pi with Puppet](http://frederickvandenbosch.be/?p=1843)
