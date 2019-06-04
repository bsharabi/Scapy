### Ip details
```
root@Secondary:~# whatis ip
ip (8)               - show / manipulate routing, network devices, interfaces and tunnels

root@Secondary:~# ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: enp2s0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc fq_codel state DOWN group default qlen 1000
    link/ether 9c:5c:8e:1c:ea:bf brd ff:ff:ff:ff:ff:ff
3: wlp3s0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
    link/ether 80:a5:89:b3:a2:53 brd ff:ff:ff:ff:ff:ff
    inet 10.0.0.103/23 brd 10.0.1.255 scope global noprefixroute wlp3s0
       valid_lft forever preferred_lft forever
    inet6 fe80::38fa:4915:7d5b:89d0/64 scope link noprefixroute
       valid_lft forever preferred_lft forever
```
### Tcpdump
Tcpdump  prints out a description of the contents of packets on a network interface that match the boolean expres‐sion; the description is preceded by a time stamp, printed, by default, as hours, minutes, seconds, and  fractions of  a  second  since  midnight.  It can also be run with the -w flag, which causes it to save the packet data to a
       file for later analysis, and/or with the -r flag, which causes it to read from a saved packet file rather than  to
       read  packets  from  a  network interface.  It can also be run with the -V flag, which causes it to read a list of
       saved packet files. In all cases, only packets that match expression will be processed by tcpdump.

```
root@Secondary:~# whatis tcpdump
tcpdump (8)          - dump traffic on a network
```

one of the used options in t6cpdump is:
```
-i interface
--interface=interface
Listen on interface.  If unspecified, tcpdump searches the system interface list for the  lowest  numbered,
configured up interface (excluding loopback), which may turn out to be, for example, ``eth0''.

On Linux systems with 2.2 or later kernels, an interface argument of ``any'' can be used to capture packets
from all interfaces.  Note that captures on the ``any'' device will not be done in promiscuous mode.

```

* in order to dump traffic on the local host, run this command:
```
sudo tcpdump -i lo
```
now, open with byobu a new tab, and run with scapy:
```
>>> sr1(IP(dst="127.0.0.1",src="8.8.4.4")/ICMP())
Begin emission:
Finished sending 1 packets.
```
go back to the tab that runs tcpdump, and see:
```
10:21:41.976913 IP google-public-dns-b.google.com > localhost: ICMP echo request, id 0, seq 0, length 8
```

### Tcpdump to pcap
* create a new python file, that sends 2 packets to localhost:
```
root@Secondary:~# cat > send_test.py
```
now paste this content:
```
from scapy.all import *

# send a ICMP (ping) to local host
sr1(IP(dst="127.0.0.1",src="8.8.4.4")/ICMP())
```
and save (with control+d)

* run in a new window a tcpdump that listens to localhost metwork, and saved it to pcap file:
```
root@Secondary:~# tcpdump -w test.pcap -i lo
```
* go back to the other window, and run the send_test.py file
```
root@Secondary:~# python3 send_test.py
```
* go to the tcpdump window - and stop the listening with `control+c`, now all the packets are saved to a file named `test.pcap`
* run a command that will read the `test.pcap` content:
```
tcpdump -r test.pcap
```
* craete a new python script, that reads the pcap file
```
root@Secondary:~# cat > read_test.py
```
now paste this content:
```
from scapy.all import *

# rdpcap comes from scapy and loads in our pcap file
packets = rdpcap('test.pcap')
print(packets)
for i in range(0,len(packets)):
    pkt = packets[i]
    pkt.show()

```
and save (with control+d), and run the send_test.py file
```
root@Secondary:~# python3 read_test.py
```

The outpot is:
```
<test.pcap: TCP:0 UDP:0 ICMP:1 Other:0>

  type      = 0x800
###[ IP ]###
     version   = 4
     ihl       = 5
     tos       = 0x0
     len       = 28
     id        = 1
     flags     =
     frag      = 0
     ttl       = 64
     proto     = icmp
     chksum    = 0xefd3
     src       = 8.8.4.4
     dst       = 127.0.0.1
     \options   \
###[ ICMP ]###
        type      = echo-request
        code      = 0
        chksum    = 0xf7ff
        id        = 0x0
        seq       = 0x0
```
