from scapy.all import *
import re

# rdpcap comes from scapy and loads in our pcap file
packets = rdpcap('CaptureFile.pcap')

print("------------------------- Result-08-------------------------")

print(len(packets[0]))

print(packets[1][Raw].show())