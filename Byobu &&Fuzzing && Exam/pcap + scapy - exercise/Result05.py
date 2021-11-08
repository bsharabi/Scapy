from scapy.all import *
import re

# rdpcap comes from scapy and loads in our pcap file
packets = rdpcap('CaptureFile.pcap')
print("------------------------- Result-05 -------------------------")
imin=len(packets[0])
index_=0
for i,x in enumerate(packets):
    #print("The id of packest : {} Len is {} ".format(x,len(packets[x])))
    if(imin>len(x)):
        imin=len(x)
        index_=i
print("ID : {} The Shortset packest is :{}".format(index_,imin))
print("-------------------------------------------------------------")