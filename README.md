# Scapy
Scapy is a powerful interactive packet manipulation program. It is able to forge or decode packets of a wide number of protocols, send them on the wire, capture them, match requests and replies, and much more. It can easily handle most classical tasks like scanning, tracerouting, probing, unit tests, attacks or network discovery (it can replace hping, 85% of nmap, arpspoof, arp-sk, arping, tcpdump, tshark, p0f, etc.). It also performs very well at a lot of other specific tasks that most other tools can’t handle, like sending invalid frames, injecting your own 802.11 frames, combining technics (VLAN hopping+ARP cache poisoning, VOIP decoding on WEP encrypted channel, …), etc.

Scapy runs natively on Linux, Windows, OSX and on most Unixes with libpcap (see scapy’s installation page). The same code base now runs natively on both Python 2 and Python 3.

## Introduction & install
***
  - [00_Install scapy (linux).md](https://github.com/bsharabi/Scapy/blob/master/Introduction%20%26%20install/00_Install%20scapy%20(linux).md)
  - [01_TCP and IP.md](https://github.com/bsharabi/Scapy/tree/master/Introduction%20%26%20install/01_TCP%20and%20IP.md)
  - [02_ICMP.md](https://github.com/bsharabi/Scapy/tree/master/Introduction%20%26%20install/02_ICMP.md)
  - [03_Sniff.md](https://github.com/bsharabi/Scapy/tree/master/Introduction%20%26%20install/03_Sniff.md)
## Scapy basic & Dns || UDP || TCP
***
  - [00_Scapy - basic exercises.pdf](https://github.com/bsharabi/Scapy/tree/master/Scapy%20basic%20%26%20DNS%20%26%20UDP%20-%20TCP/00_Scapy%20-%20basic%20exercises.pdf)
  - [01_Scapy - basic exercises answers.pdf](https://github.com/bsharabi/Scapy/tree/master/Scapy%20basic%20%26%20DNS%20%26%20UDP%20-%20TCP/01_Scapy%20-%20basic%20exercises%20answers.pdf)
  - [02_DNS.md](https://github.com/bsharabi/Scapy/tree/master/Scapy%20basic%20%26%20DNS%20%26%20UDP%20-%20TCP/02_DNS.md)
  - [03_Dig command.md](https://github.com/bsharabi/Scapy/tree/master/Scapy%20basic%20%26%20DNS%20%26%20UDP%20-%20TCP/03_Dig%20command.md)
  - [04_udp in tcp-ip.gif](https://github.com/bsharabi/Scapy/tree/master/Scapy%20basic%20%26%20DNS%20%26%20UDP%20-%20TCP/04_udp%20in%20tcp-ip.gif)
  - [05_DNS with scapy.md](https://github.com/bsharabi/Scapy/tree/master/Scapy%20basic%20%26%20DNS%20%26%20UDP%20-%20TCP/05_DNS%20with%20scapy.md)
## Byobu fuzzing and example
***
  - [00_byobu.md](https://github.com/bsharabi/Scapy/tree/master/Day%2003%20-%2002.04.2019/00_byobu.md)
  - [00_fuzzing.md](https://github.com/bsharabi/Scapy/tree/master/Day%2003%20-%2002.04.2019/00_fuzzing.md)
  - [01_tcpdump and pcap.md](https://github.com/bsharabi/Scapy/tree/master/Day%2003%20-%2002.04.2019/01_tcpdump%20and%20pcap.md)
  - [app12.py](https://github.com/bsharabi/Scapy/tree/master/Day%2003%20-%2002.04.2019/app12.py)
  - [pcap + scapy - exercise](https://github.com/bsharabi/Scapy/tree/master/Day%2003%20-%2002.04.2019/pcap%20+%20scapy%20-%20exercise)
    - [a.py](https://github.com/bsharabi/Scapy/tree/master/Day%2003%20-%2002.04.2019/pcap%20+%20scapy%20-%20exercise/a.py)
    - [CaptureFile.cap](https://github.com/bsharabi/Scapy/tree/master/Day%2003%20-%2002.04.2019/pcap%20+%20scapy%20-%20exercise/CaptureFile.cap)
    - [pcap + scapy - exercise.pdf](https://github.com/bsharabi/Scapy/tree/master/Day%2003%20-%2002.04.2019/pcap%20+%20scapy%20-%20exercise/pcap%20+%20scapy%20-%20exercise.pdf)
    - [Readme.md](https://github.com/bsharabi/Scapy/tree/master/Day%2003%20-%2002.04.2019/pcap%20+%20scapy%20-%20exercise/Readme.md)
    - [Result01.py](https://github.com/bsharabi/Scapy/tree/master/Day%2003%20-%2002.04.2019/pcap%20+%20scapy%20-%20exercise/Result01.py)
    - [Result02.py](https://github.com/bsharabi/Scapy/tree/master/Day%2003%20-%2002.04.2019/pcap%20+%20scapy%20-%20exercise/Result02.py)
    - [Result03.py](https://github.com/bsharabi/Scapy/tree/master/Day%2003%20-%2002.04.2019/pcap%20+%20scapy%20-%20exercise/Result03.py)
    - [Result04.py](https://github.com/bsharabi/Scapy/tree/master/Day%2003%20-%2002.04.2019/pcap%20+%20scapy%20-%20exercise/Result04.py)
    - [Result05.py](https://github.com/bsharabi/Scapy/tree/master/Day%2003%20-%2002.04.2019/pcap%20+%20scapy%20-%20exercise/Result05.py)
    - [Result06.py](https://github.com/bsharabi/Scapy/tree/master/Day%2003%20-%2002.04.2019/pcap%20+%20scapy%20-%20exercise/Result06.py)
  - [read_test.py](https://github.com/bsharabi/Scapy/tree/master/Day%2003%20-%2002.04.2019/read_test.py)
  - [send_test.py](https://github.com/bsharabi/Scapy/tree/master/Day%2003%20-%2002.04.2019/send_test.py)
  - [send_test2 _withSendp.py](https://github.com/bsharabi/Scapy/tree/master/Day%2003%20-%2002.04.2019/send_test2%20_withSendp.py)
  - [send_test2.py](https://github.com/bsharabi/Scapy/tree/master/Day%2003%20-%2002.04.2019/send_test2.py)
  - [send_test_withSendp..py](https://github.com/bsharabi/Scapy/tree/master/Day%2003%20-%2002.04.2019/send_test_withSendp..py)
## Read import\export and sniff
***
  - [00_read and write pcap with scapy.md](https://github.com/bsharabi/Scapy/tree/master/Day%2004%20-%2016.04.2019/00_read%20and%20write%20pcap%20with%20scapy.md)
  - [01_Importing and Exporting PCAP Data.pdf](https://github.com/bsharabi/Scapy/tree/master/Day%2004%20-%2016.04.2019/01_Importing%20and%20Exporting%20PCAP%20Data.pdf)
  - [02_sniff options in scapy.md](https://github.com/bsharabi/Scapy/tree/master/Day%2004%20-%2016.04.2019/02_sniff%20options%20in%20scapy.md)
  - [app00.py](https://github.com/bsharabi/Scapy/tree/master/Day%2004%20-%2016.04.2019/app00.py)
## Exam
***
  - [Exam.md](https://github.com/bsharabi/Scapy/tree/master/Day%2005%20-%2023.05.2019/Exam.md)
  - [scapy summary.pdf](https://github.com/bsharabi/Scapy/tree/master/Day%2005%20-%2023.05.2019/scapy%20summary.pdf)
