from scapy.all import *
import re

# rdpcap comes from scapy and loads in our pcap file
packets = rdpcap('CaptureFile.pcap')
print("------------------------- Result-04 -------------------------")
imax=0
index=0
for i,x in enumerate(packets):
    #print("The id of packest : {} Len is {} ".format(x,len(packets[x])))
    if(imax<len(x)):
        imax=len(x)
        index=i
print("ID : {} The longset packest is :{}".format(index,imax))
print("-------------------------------------------------------------")
