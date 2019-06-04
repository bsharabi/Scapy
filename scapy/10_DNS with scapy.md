## Steps to get dns packet:
* In scapy run:
 ```
a=sniff(50)
```
* In another shell run:
```
anna@HP-Printer:~$ host canada.com
```
* Go back to scapy shell and run:
```
a.summary()
Ether / IP / TCP 216.58.206.14:https > 10.0.0.106:36338 PA / Raw
Ether / IP / TCP 216.58.206.14:https > 10.0.0.106:36338 PA / Raw
Ether / IP / TCP 10.0.0.106:36338 > 216.58.206.14:https A
Ether / IP / UDP / DNS Qry "b'canada.com.'" 
Ether / IP / TCP 216.58.206.14:https > 10.0.0.106:36338 PA / Raw
Ether / IP / UDP / DNS Ans "199.71.40.135" 
Ether / IP / UDP / DNS Qry "b'canada.com.'" 
Ether / IP / TCP 10.0.0.106:36338 > 216.58.206.14:https A
Ether / IP / UDP / DNS Ans 
Ether / IP / UDP / DNS Qry "b'canada.com.'" 
Ether / IP / UDP / DNS Ans "b'\x00\x00\x00'" 
Ether / IP / TCP 10.0.0.106:48468 > 151.101.14.180:https A
```
* Save the fourth packet that we sniffed before:
```
b=a[3]
```
* Get all the details of the packet that is stored in b:
```
b.show()
###[ Ethernet ]### 
  dst= c4:e9:84:d0:41:ac
  src= e4:70:b8:4b:f2:f3
  type= 0x800
###[ IP ]### 
     version= 4
     ihl= 5
     tos= 0x0
     len= 56
     id= 59106
     flags= 
     frag= 0
     ttl= 64
     proto= udp
     chksum= 0x8767
     src= 10.0.0.106
     dst= 1.1.1.1
     \options\
###[ UDP ]### 
        sport= 38052
        dport= domain
        len= 36
        chksum= 0x8a77
###[ DNS ]### 
           id= 55357
           qr= 0
           opcode= QUERY
           aa= 0
           tc= 0
           rd= 1
           ra= 0
           z= 0
           ad= 0
           cd= 0
           rcode= ok
           qdcount= 1
           ancount= 0
           nscount= 0
           arcount= 0
           \qd\
            |###[ DNS Question Record ]### 
            |  qname= 'canada.com.'
            |  qtype= A
            |  qclass= IN
           an= None
           ns= None
           ar= None
```
* Now we want to edit the `qname` that is in `DNS.qd`:
```
print(b[DNS].qname)
canada.com.
```


* 
Note: ports `53` is the default for the `domain`
```
answer = sr1(IP(dst="1.1.1.1")/UDP(dport=53)/DNS(rd=1,qd=DNSQR(qname="www.ynet.co.il")),verbose=0)

answer.show()
###[ IP ]### 
  version= 4
  ihl= 5
  tos= 0x28
  len= 150
  id= 3830
  flags= DF
  frag= 0
  ttl= 56
  proto= udp
  chksum= 0x26ce
  src= 1.1.1.1
  dst= 10.0.0.106
  \options\
###[ UDP ]### 
     sport= domain
     dport= domain
     len= 130
     chksum= 0x70ee
###[ DNS ]### 
        id= 0
        qr= 1
        opcode= QUERY
        aa= 0
        tc= 0
        rd= 1
        ra= 1
        z= 0
        ad= 0
        cd= 0
        rcode= ok
        qdcount= 1
        ancount= 3
        nscount= 0
        arcount= 0
        \qd\
         |###[ DNS Question Record ]### 
         |  qname= 'www.ynet.co.il.'
         |  qtype= A
         |  qclass= IN
        \an\
         |###[ DNS Resource Record ]### 
         |  rrname= 'www.ynet.co.il.'
         |  type= CNAME
         |  rclass= IN
         |  ttl= 110
         |  rdlen= 28
         |  rdata= 'www.ynet.co.il.edgekey.net.'
         |###[ DNS Resource Record ]### 
         |  rrname= 'www.ynet.co.il.edgekey.net.'
         |  type= CNAME
         |  rclass= IN
         |  ttl= 8473
         |  rdlen= 25
         |  rdata= 'e12476.b.akamaiedge.net.'
         |###[ DNS Resource Record ]### 
         |  rrname= 'e12476.b.akamaiedge.net.'
         |  type= A
         |  rclass= IN
         |  ttl= 10
         |  rdlen= 4
         |  rdata= '2.18.235.16'
        ns= None
        ar= None

```