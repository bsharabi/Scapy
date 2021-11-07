# Steps to run scapy in Linux(deb)

## Step 1 - change user to root
```bash
anna@HP-Printer:~$ sudo -i  # change the user to root user
```

## Step 2 - install python and pip
```
root@HP-Printer:~# apt update
root@HP-Printer:~# apt install python3
root@HP-Printer:~# apt install python3-pip
```

## Step 3 - check if python and pip are installed successfully
```
root@HP-Printer:~# whatis python3
python3 (1)          - an interpreted, interactive, object-oriented programming language


root@HP-Printer:~# whatis pip3
pip3 (1)             - A tool for installing and managing Python packages
```

## Step 4 - install scapy
* If we installed pip:
```
root@HP-Printer:~# pip3 search scapy
scapy (2.4.2)                        - Scapy: interactive packet manipulation tool


root@HP-Printer:~# pip3 install scapy
```
* If we did not installed pip:
```
root@HP-Printer:~# apt search scapy
root@HP-Printer:~# apt install python3-scapy
```

## Step 5 - run scapy
* first option to run scapy (from python):
```
root@HP-Printer:~# python3
>>> from scapy.all import * 
```
* second option to run scapy (from scapy):
```
root@HP-Printer:~# scapy
```