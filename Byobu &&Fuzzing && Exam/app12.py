from scapy.all import *

# rdpcap comes from scapy and loads in our pcap file
packets = rdpcap('CaptureFile.cap')
print(packets)