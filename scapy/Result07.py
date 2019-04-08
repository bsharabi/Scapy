from scapy.all import *
import re

# rdpcap comes from scapy and loads in our pcap file
packets = rdpcap('CaptureFile.pcap')
print("------------------------- Result-07-------------------------")
listUsers=[]
for x in packets:    
    if("user" in str(x) or "pass" in str(x)):
        #print("-----------------------------------")
        temp=str(x)
        #print(temp)
        lenTemp=temp.find("user")
        NewStr=""
        while(lenTemp!=-1 and temp[lenTemp]!='\\'):
            NewStr+=temp[lenTemp]
            lenTemp+=1
        listUsers.append(NewStr)
        lenTemp=temp.find("pass")
        NewStr=""
        while(lenTemp!=-1 and temp[lenTemp]!='\\'):
            NewStr+=(temp[lenTemp])
            lenTemp+=1
        listUsers.append(NewStr)
        #print("-----------------------------------")
print(listUsers)
print("------------------------------------------------------------")
