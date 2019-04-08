from scapy.all import *
import re

# rdpcap comes from scapy and loads in our pcap file
packets = rdpcap('CaptureFile.pcap')
print("------------------------- Result-06 -------------------------")
listHost=[]
for i,x in enumerate(packets):     
    strHost=""  
    if("GET" in str(x)):
        
        # Method 1 with a regex
        strHost=re.search(r'\\r\\nHost: (.*?)\\r\\n',str(x)).group(1)
        # Method 2 with a loop 
        '''
        hostStr=str(x[Raw])
        len1=hostStr.find("Host")
        while(hostStr[len1]!='\\'and hostStr[len1+1]!='r'):
            strHost+=hostStr[len1]
            len1+=1
        '''
        listHost.append(strHost) 
print(',\n'.join(listHost))
print(len(listHost))
print("-------------------------------------------------------------")