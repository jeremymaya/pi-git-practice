# Raspberry Pi OS

Author: Kyungrae Kim

This is a repository created from Raspberry Pi OS. I will be using this repository to become more familiar with Linux.

---

## Table of Contents

* [Server Management](/scripts)
  * System Health Check
* [Flask Application](/flask_app)
  * Turn on WoL enabled computer with Google Assistant
* [Configuration Management with Puppet](/#)
  * _Coming Soon_

---

## Using Raspberry Pi OS Headless

### Remote Access

Raspberry Pi OS can be accessed remotely using [SSH (Secure Shell)](https://www.raspberrypi.org/documentation/remote-access/ssh/README.md), which allows user to access the command line of a Raspberry Pi remotely from another computer or device on the same network.

Refer to [Setting up a Raspberry Pi headless](https://www.raspberrypi.org/documentation/configuration/wireless/headless.md) in order to set up the Pi OS without a monitor or keyboard.

### Remote Development using SSH

Instead of using ```nano``` or other CLI based editors, [Visual Studio Code Remote - SSH extension](https://code.visualstudio.com/docs/remote/ssh) allows users to open a remote folder on any remote machine, virtual machine, or container with a running SSH server and take full advantage of VS Code's feature set.

---

## Change Log

* *Table of Contents added* - 17 September 2020
* *Initial setup* - 11 June 2020