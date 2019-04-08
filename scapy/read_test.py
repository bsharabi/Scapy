from scapy.all import *

# rdpcap comes from scapy and loads in our pcap file
packets = rdpcap('test.pcap')
print(packets)

pkt = packets[0]
print(pkt.fields['subtype'])
pkt.show()
