from scapy.all import *
import re

# rdpcap comes from scapy and loads in our pcap file
packets = rdpcap('CaptureFile.pcap')
print("------------------------- Result-01 -------------------------")
# Result a
FirstPks= packets[0]
print(FirstPks)
# Result b
print(len(FirstPks))
print("-------------------------------------------------------------")
