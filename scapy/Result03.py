from scapy.all import *
import re

# rdpcap comes from scapy and loads in our pcap file
packets = rdpcap('CaptureFile.pcap')

print("------------------------- Result-03 -------------------------")
print(len(packets))
print("-------------------------------------------------------------")
