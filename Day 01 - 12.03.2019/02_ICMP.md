# ICMP
The Internet Control Message Protocol (ICMP) is a supporting protocol in the Internet protocol suite.    

ICMP differs from transport protocols such as TCP and UDP in that it is not typically used to exchange data between systems, nor is it regularly employed by end-user network applications (with the exception of some diagnostic tools like ping and traceroute).

#### With scapy, we can check all the headers (properties) of ICMP:
```
ls(ICMP())
type       : ByteEnumField                       = 8               (8)
code       : MultiEnumField (Depends on type)    = 0               (0)
chksum     : XShortField                         = None            (None)
id         : XShortField (Cond)                  = 0               (0)
seq        : XShortField (Cond)                  = 0               (0)
ts_ori     : ICMPTimeStampField (Cond)           = 72604595        (72604595)
ts_rx      : ICMPTimeStampField (Cond)           = 72604595        (72604595)
ts_tx      : ICMPTimeStampField (Cond)           = 72604595        (72604595)
gw         : IPField (Cond)                      = '0.0.0.0'       ('0.0.0.0')
ptr        : ByteField (Cond)                    = 0               (0)
reserved   : ByteField (Cond)                    = 0               (0)
length     : ByteField (Cond)                    = 0               (0)
addr_mask  : IPField (Cond)                      = '0.0.0.0'       ('0.0.0.0')
nexthopmtu : ShortField (Cond)                   = 0               (0)
unused     : ShortField (Cond)                   = 0               (0)
unused     : IntField (Cond)                     = 0               (0)
```

#### Create and send a ping request - without waiting for response
```
a=IP(dst="8.8.8.8")/ICMP()
sendp(a)

.
Sent 1 packets.
```

#### Create and send a ping request - with waiting for response
```
a=IP(dst="8.8.8.8")/ICMP()
sr1(a) #send recive 1 - here we wait for the response


Begin emission:
.Finished sending 1 packets.
.*
Received 3 packets, got 1 answers, remaining 0 packets
<IP  version=4 ihl=5 tos=0xb8 len=28 id=47258 flags= frag=0 ttl=120 proto=icmp chksum=0x6c41 src=8.8.8.8 dst=10.6.3.56 |<ICMP  type=echo-reply code=0 chksum=0x0 id=0x0 seq=0x0 |<Padding  load='\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' |>>>
```


#### Create and send a ping request with another (spoofed) src IP address
```
sr1(IP(dst="8.8.8.8", src="8.8.4.4")/ICMP())

Begin emission:
.Finished sending 1 packets.
.................................................................................................................................................................^C
Received 162 packets, got 0 answers, remaining 1 packets
```
