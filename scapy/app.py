from scapy.all import *

# rdpcap comes from scapy and loads in our pcap file
packets = rdpcap('CaptureFile.pcap')
cnt=0
cnt1=0
'''
for i in range(0,len(packets)):
    try:
        if('ynet' in str(packets[i][DNS][1].qname)):
            print(packets[i][DNS][1].qname)   
            cnt+=1 
    except:
        pass
        
print(cnt)

for i in range(0,len(packets)):
    if(cnt1>=11):
        break
    if "ynet" in str(packets[i]):
        print(packets[i].show())
        cnt1+=1
'''
print(cnt1)
print(len(packets[0]))
#print(packets[4].show())
for i in range(0,len(packets)):
    if(cnt1>=2):
        break
    if "GET" in str(packets[i]):
        print(packets[i].Host())
        print("----------------------")
        cnt1+=1

#for i in range(0,len(packets)):


#print(packets[0][IP])
'''
for i in range(0,len(packets)):
    pkt = packets[i]
    pkt.show()
'''