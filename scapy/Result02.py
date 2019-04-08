from scapy.all import *
import re

# rdpcap comes from scapy and loads in our pcap file
packets = rdpcap('CaptureFile.pcap')

print("------------------------- Result-02 -------------------------")
listCnt={"google":0,"ynet":0,"SuperPharmLogo.gif":0,"HelloWorld":0}
for x in packets:
    for z in listCnt:
        if z in str(x):
            listCnt[z]+=1

print(listCnt)
print("-------------------------------------------------------------")
