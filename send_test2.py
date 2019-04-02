from scapy.all import *

# send a ICMP (ping) to local host
sr1(IP(dst="127.0.0.1",src="8.8.4.4")/ICMP())


# send a ICMP (ping) to local host 
sr1(IP(dst="127.0.0.1",src="1.1.1.1")/ICMP())
