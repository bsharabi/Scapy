from scapy.all import *
import re




# rdpcap comes from scapy and loads in our pcap file
packets = rdpcap('CaptureFile.pcap')
a=max(packets)
print(len(a))
print(max(packets))
#"------------------------- Result-01 -------------------------"
print("------------------------- Result-01 -------------------------")
# Result a
FirstPks= packets[0]
print(FirstPks)
# Result b
print(len(FirstPks))
print("-------------------------------------------------------------")
print("------------------------- Result-02 -------------------------")
listCnt={"google":0,"ynet":0,"SuperPharmLogo.gif":0,"HelloWorld":0}
for x in packets:
    for z in listCnt:
        if z in str(x):
            listCnt[z]+=1

print(listCnt)
print("-------------------------------------------------------------")
print("------------------------- Result-03 -------------------------")
print(len(packets))
print("-------------------------------------------------------------")
print("------------------------- Result-04 -------------------------")
imax=0
index=0
for x in range(len(packets)):
    #print("The id of packest : {} Len is {} ".format(x,len(packets[x])))
    if(imax<len(packets[x])):
        imax=len(packets[x])
        index=x+1
print("ID : {} The longset packest is :{}".format(index,imax))
print("-------------------------------------------------------------")
print("------------------------- Result-05 -------------------------")
imin=len(packets[0])
index_=0
for x in range(len(packets)):
    #print("The id of packest : {} Len is {} ".format(x,len(packets[x])))
    if(imin>len(packets[x])):
        imin=len(packets[x])
        index_=x+1
print("ID : {} The Shortset packest is :{}".format(index_,imin))
print("-------------------------------------------------------------")
print("------------------------- Result-06 -------------------------")
listHost=[]
for x in range(len(packets)):       
    if("GET" in str(packets[x])):
        # Method 1
        strHost=re.search(r'\\r\\nHost: (.*?)\\r\\n',str(packets[x])).group(1)
        # Method 2
        '''
        hostStr=str(packets[x][Raw])
        len1=hostStr.find("Host")
        while(hostStr[len1]!='\\'and hostStr[len1+1]!='r'):
            strHost+=(hostStr[len1])
            len1+=1
        '''
        listHost.append(strHost) 
print(',\n'.join(listHost))
print(len(listHost))
print("-------------------------------------------------------------")
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

print("------------------------- Result-08-------------------------")
dnsList=[]
for i,pkt in enumerate(packets):
    if DNS in pkt:
        dnsList.append(pkt["DNS"].id)


for x in packets:    
   if DNS in x:
        print("------------------------------------")
        x.show()      
        print("------------------------------------")
     
print(dnsList)
print("------------------------------------------------------------")
