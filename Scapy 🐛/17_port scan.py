import random
from scapy.all import ICMP, IP, sr1, TCP, fuzz
 
# Define end host and TCP port range
host = "1.1.1.1"
port_range = [22, 23, 80, 443, 3389]
 
# Send SYN with random Src Port for each Dst port
for dst_port in port_range:
    src_port = random.randint(1025,65534)
    resp = sr1(IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags="S"),timeout=1,verbose=0)
 
    if resp is None:
        print(f"{host}:{dst_port} is filtered (silently dropped).")
 
    elif(resp.haslayer(TCP)):
        if(resp.getlayer(TCP).flags == "SA"):
            # Send a gratuitous RST to close the connection
            send_rst = sr1(IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags='R'),timeout=1,verbose=0)
            print(f"{host}:{dst_port} is open.")

