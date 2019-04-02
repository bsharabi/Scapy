#### install curl 
```
anna@HP-Printer:~$ apt install curl

anna@HP-Printer:~$ whatis curl
curl (1)             - transfer a URL
```

#### Start sniffing in scapy
* in scapy shell:
```
a=sniff(20)
```
* afterwards, run in another window:
```
anna@HP-Printer:~$ curl https://www.google.com/
```
* then go back to scapy shell and run:
```
print(a)


<Sniffed: TCP:0 UDP:6 ICMP:0 Other:14>
```
* now get the summery of the sniffed packages:
```
a.summary()


Ether / IPv6 / ICMPv6ND_RA / ICMPv6 Neighbor Discovery Option - Source Link-Layer Address c4:e9:84:d0:41:ac
Ether / IP / UDP / DNS Qry "b'google.com.'" 
Ether / IP / UDP / DNS Qry "b'google.com.'" 
Ether / IP / UDP / DNS Ans "172.217.21.206" 
Ether / IP / UDP / DNS Ans "2a00:1450:4001:80b::200e" 
Ether / IP / TCP 10.0.0.106:37454 > 172.217.21.206:http S
Ether / IPv6 / TCP fe80::731:f2ea:d389:ec42:44310 > 2a00:1450:4001:80b::200e:http S
Ether / IPv6 / ICMPv6ND_NS / ICMPv6 Neighbor Discovery Option - Source Link-Layer Address c4:e9:84:d0:41:ac
Ether / IPv6 / ICMPv6ND_NA / ICMPv6 Neighbor Discovery Option - Destination Link-Layer Address e4:70:b8:4b:f2:f3
Ether / IP / TCP 172.217.21.206:http > 10.0.0.106:37454 SA / Padding
Ether / IP / TCP 10.0.0.106:37454 > 172.217.21.206:http A
Ether / fe80::90f0:80ff:fe54:b31a > fe80::731:f2ea:d389:ec42 (58) / ICMPv6DestUnreach / IPerror6 / TCPerror
Ether / IP / TCP 10.0.0.106:37454 > 172.217.21.206:http PA / Raw
Ether / IP / TCP 172.217.21.206:http > 10.0.0.106:37454 PA / Raw
Ether / IP / TCP 10.0.0.106:37454 > 172.217.21.206:http A
Ether / IP / TCP 10.0.0.106:37454 > 172.217.21.206:http FA
Ether / IP / TCP 172.217.21.206:http > 10.0.0.106:37454 FA / Padding
Ether / IP / TCP 10.0.0.106:37454 > 172.217.21.206:http A
Ether / IPv6 / ICMPv6ND_RA / ICMPv6 Neighbor Discovery Option - Source Link-Layer Address c4:e9:84:d0:41:ac
Ether / IP / UDP 10.0.0.106:60090 > 173.194.76.189:443 / Raw
```
* We want to access the packet in index 5
```
ls(a[5])

dst        : DestMACField                        = 'c4:e9:84:d0:41:ac' (None)
src        : SourceMACField                      = 'e4:70:b8:4b:f2:f3' (None)
type       : XShortEnumField                     = 2048            (36864)
--
version    : BitField (4 bits)                   = 4               (4)
ihl        : BitField (4 bits)                   = 5               (None)
tos        : XByteField                          = 0               (0)
len        : ShortField                          = 60              (None)
id         : ShortField                          = 38980           (1)
flags      : FlagsField (3 bits)                 = <Flag 2 (DF)>   (<Flag 0 ()>)
frag       : BitField (13 bits)                  = 0               (0)
ttl        : ByteField                           = 64              (64)
proto      : ByteEnumField                       = 6               (0)
chksum     : XShortField                         = 54630           (None)
src        : SourceIPField                       = '10.0.0.106'    (None)
dst        : DestIPField                         = '172.217.21.206' (None)
options    : PacketListField                     = []              ([])
--
sport      : ShortEnumField                      = 37454           (20)
dport      : ShortEnumField                      = 80              (80)
seq        : IntField                            = 4228648855      (0)
ack        : IntField                            = 0               (0)
dataofs    : BitField (4 bits)                   = 10              (None)
reserved   : BitField (3 bits)                   = 0               (0)
flags      : FlagsField (9 bits)                 = <Flag 2 (S)>    (<Flag 2 (S)>)
window     : ShortField                          = 29200           (8192)
chksum     : XShortField                         = 38950           (None)
urgptr     : ShortField                          = 0               (0)
options    : TCPOptionsField                     = [('MSS', 1460), ('SAckOK', b''), ('Timestamp', (3167163822, 0)), ('NOP', None), ('WScale', 7)] (b'')
```

* Store this packet to a variable (so it will be easy to access the headers of this packet)
```
b=a[5]
ls(b)


dst        : DestMACField                        = 'c4:e9:84:d0:41:ac' (None)
src        : SourceMACField                      = 'e4:70:b8:4b:f2:f3' (None)
type       : XShortEnumField                     = 2048            (36864)
--
version    : BitField (4 bits)                   = 4               (4)
ihl        : BitField (4 bits)                   = 5               (None)
tos        : XByteField                          = 0               (0)
len        : ShortField                          = 60              (None)
id         : ShortField                          = 38980           (1)
flags      : FlagsField (3 bits)                 = <Flag 2 (DF)>   (<Flag 0 ()>)
frag       : BitField (13 bits)                  = 0               (0)
ttl        : ByteField                           = 64              (64)
proto      : ByteEnumField                       = 6               (0)
chksum     : XShortField                         = 54630           (None)
src        : SourceIPField                       = '10.0.0.106'    (None)
dst        : DestIPField                         = '172.217.21.206' (None)
options    : PacketListField                     = []              ([])
--
sport      : ShortEnumField                      = 37454           (20)
dport      : ShortEnumField                      = 80              (80)
seq        : IntField                            = 4228648855      (0)
ack        : IntField                            = 0               (0)
dataofs    : BitField (4 bits)                   = 10              (None)
reserved   : BitField (3 bits)                   = 0               (0)
flags      : FlagsField (9 bits)                 = <Flag 2 (S)>    (<Flag 2 (S)>)
window     : ShortField                          = 29200           (8192)
chksum     : XShortField                         = 38950           (None)
urgptr     : ShortField                          = 0               (0)
options    : TCPOptionsField                     = [('MSS', 1460), ('SAckOK', b''), ('Timestamp', (3167163822, 0)), ('NOP', None), ('WScale', 7)] (b'')
```

* Now - lets access the IP src address of this packet:
```
print(b[IP].src)

'10.0.0.106'
```
* And the next step - is to change this ip src address:
```
b[IP].src="8.8.4.4"
ls(b)


dst        : DestMACField                        = 'c4:e9:84:d0:41:ac' (None)
src        : SourceMACField                      = 'e4:70:b8:4b:f2:f3' (None)
type       : XShortEnumField                     = 2048            (36864)
--
version    : BitField (4 bits)                   = 4               (4)
ihl        : BitField (4 bits)                   = 5               (None)
tos        : XByteField                          = 0               (0)
len        : ShortField                          = 60              (None)
id         : ShortField                          = 38980           (1)
flags      : FlagsField (3 bits)                 = <Flag 2 (DF)>   (<Flag 0 ()>)
frag       : BitField (13 bits)                  = 0               (0)
ttl        : ByteField                           = 64              (64)
proto      : ByteEnumField                       = 6               (0)
chksum     : XShortField                         = 54630           (None)
src        : SourceIPField                       = '8.8.4.4'       (None)
dst        : DestIPField                         = '172.217.21.206' (None)
options    : PacketListField                     = []              ([])
--
sport      : ShortEnumField                      = 37454           (20)
dport      : ShortEnumField                      = 80              (80)
seq        : IntField                            = 4228648855      (0)
ack        : IntField                            = 0               (0)
dataofs    : BitField (4 bits)                   = 10              (None)
reserved   : BitField (3 bits)                   = 0               (0)
flags      : FlagsField (9 bits)                 = <Flag 2 (S)>    (<Flag 2 (S)>)
window     : ShortField                          = 29200           (8192)
chksum     : XShortField                         = 38950           (None)
urgptr     : ShortField                          = 0               (0)
options    : TCPOptionsField                     = [('MSS', 1460), ('SAckOK', b''), ('Timestamp', (3167163822, 0)), ('NOP', None), ('WScale', 7)] (b'')
```
* Send this packet:
```
sendp(b)

.
Sent 1 packets.
```
