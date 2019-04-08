from scapy.all import *

# send a ICMP (ping) to local host - from google
sr1(IP(dst="127.0.0.1",src="8.8.4.4")/ICMP())

# send a DNS request to local hoste
sr1(IP(dst="127.0.0.1")/UDP(dport=53)/DNS(rd=1,qd=DNSQR(qname="www.google.com")),verbose=0)
