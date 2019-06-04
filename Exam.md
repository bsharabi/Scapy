
### Question 1
Given the following code:
```python
from scapy.all import *
a=input("enter IP or url: ")
sendp(IP(dst=a)/ICMP())
```
explain what this code does
### Answer 1
gets from the user an ip address, and sends a ping to this address

### Question 2
write the code that sends a ping from `1.1.1.1` to  `2.2.2.2`
### Answer 2
```python
sendp(IP(src="1.1.1.1",dst="2.2.2.2")/ICMP())
```

### Question 3
write the code that sends a ping from `1.1.1.1` to  `2.2.2.2`, and gets the answer
### Answer 3
```python
sr1(IP(src="1.1.1.1",dst="2.2.2.2")/ICMP())
```
### Question 4
write the code that sends a DNS request to `1.1.1.1:53` in order to get the address of `www.ynet.co.il`, and gets the answer
### Answer 4
```python
sr1(IP(dst="1.1.1.1")/UDP(dport=53)/DNS(qd=DNSQR(qname="www.ynet.co.il")))
```

### Question 5
Given the following code:
```python
from scapy.all import sniff, UDP, TCP

def custom_action(packet):
    res=""
    if packet.getlayer(UDP)!=None:
        print(packet)
        res=packet["UDP"].sport
    elif packet.getlayer(TCP)!=None:
        res=packet["TCP"].flags
    return res 

sniff(filter="ip", prn=custom_action, count=10)
```
explain what this code does
### Answer 5
sniffs 10 packets, and prints for each packet:
    * the flags (if the packet is a `TCP` packet)
    * the sport (if the packet is an `UDP` packet)