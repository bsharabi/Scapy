# Sniffing analysis with Python


## Result 1
```python
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


```
## Result 2
```python
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
```
## Result 3
```python
from scapy.all import *
import re

# rdpcap comes from scapy and loads in our pcap file
packets = rdpcap('CaptureFile.pcap')

print("------------------------- Result-03 -------------------------")
print(len(packets))
print("-------------------------------------------------------------")
```
## Result 4
```python
from scapy.all import *
import re

# rdpcap comes from scapy and loads in our pcap file
packets = rdpcap('CaptureFile.pcap')
print("------------------------- Result-04 -------------------------")
imax=packets[0]
index=0
for i,x in enumerate(packets):
    #print("The id of packest : {} Len is {} ".format(x,len(packets[x])))
    if(imax<len(x)):
        imax=len(x)
        index=i
print("ID : {} The longset packest is :{}".format(index,imax))
print("-------------------------------------------------------------")
```
## Result 5
```python
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
```
## Result 6
```python
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

```