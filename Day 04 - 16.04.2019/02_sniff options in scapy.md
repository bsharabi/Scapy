# `sniff` function

`sniff` - is a `Scapy` function to sniff packets and return a list of packets.   

The decleration of this function is:

```python
def sniff(count=0, store=True, offline=None, prn=None, lfilter=None,
          L2socket=None, timeout=None, opened_socket=None,
          stop_filter=None, iface=None, started_callback=None, *arg, **karg)
```

## Arguments of this function

Note: The iface, offline and opened_socket parameters can be either an
element, a list of elements, or a dict object mapping an element to a
label.

### count
`count` - number of packets to capture. 0 means infinity.   

for example:
```
>>> a1=sniff(count=20)
>>> print(a1)
<Sniffed: TCP:0 UDP:19 ICMP:0 Other:1>

>>> a2=sniff(count=10)
>>> print(a2)
<Sniffed: TCP:0 UDP:9 ICMP:0 Other:1>
```

### store
`store` - whether to store sniffed packets or discard them.   

for example:
```
>>> a1=sniff(count=20)
>>> print(a1)
<Sniffed: TCP:2 UDP:10 ICMP:0 Other:8>

>>> a2=sniff(count=20,store=False)
>>> print(a2)
<Sniffed: TCP:0 UDP:0 ICMP:0 Other:0>
```

### timeout
`timeout` - stop sniffing after a given time (default: None).   

for example:
```
>>> a1=sniff(count=600,timeout=3)  # sniff only for 3 seconds
>>> print(a1)
<Sniffed: TCP:0 UDP:48 ICMP:0 Other:20>
```

### offline
`offline` - PCAP file (or list of PCAP files) to read packets from,instead of sniffing them

### filter
`filter` - BPF filter to apply.   

for example:
```
>>> a = sniff(20)
>>> print(a)
<Sniffed: TCP:0 UDP:15 ICMP:0 Other:5>
>>> wrpcap("test.cap",a)

>>> c1 = sniff(offline="test.cap")
>>> print(c1)
<Sniffed: TCP:0 UDP:15 ICMP:0 Other:5>

>>> c2 = sniff(offline="test.cap",filter="udp")
>>> print(c2)
<Sniffed: TCP:0 UDP:15 ICMP:0 Other:0>
```

### lfilter
`lfilter` - Python function applied to each packet to determine if further action may be done.   

for example:
```
>>> sniff(count=8,lfilter=lambda pkt: UDP in pkt)
>>> print(a1)
<Sniffed: TCP:0 UDP:8 ICMP:0 Other:0>

>>> a2=sniff(count=8,lfilter=lambda pkt: ICMP in pkt)
>>> print(a2)
<Sniffed: TCP:0 UDP:0 ICMP:8 Other:0>
```
### iface
`iface` - interface or list of interfaces (default: None for sniffing on all interfaces).   


In linux we can get our network interfaces in few ways:
```bash
anna@HP-Printer:~$ ip link
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
2: enp0s31f6: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc fq_codel state DOWN mode DEFAULT group default qlen 1000
    link/ether a4:4c:c8:73:f8:46 brd ff:ff:ff:ff:ff:ff
3: wlp3s0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP mode DORMANT group default qlen 1000
    link/ether e4:70:b8:4b:f2:f3 brd ff:ff:ff:ff:ff:ff


anna@HP-Printer:~$ netstat -i
Kernel Interface table
Iface      MTU    RX-OK RX-ERR RX-DRP RX-OVR    TX-OK TX-ERR TX-DRP TX-OVR Flg
enp0s31f  1500        0      0      0 0             0      0      0      0 BMU
lo       65536  1338839      0      0 0       1338839      0      0      0 LRU
wlp3s0    1500  8894331      0      0 0       3834117      0      0      0 BMRU

```

In order to get only the interfaces names we can run this commands:
```
anna@HP-Printer:~$ netstat -i | tail -n$[ $(netstat -i | wc -l) - 2 ] | cut -d' ' -f1
enp0s31f
lo
wlp3s0

```
now, we will run a sniff, without interface filter:
* step 1 - in scapy run:
    ```
    >>> a1=sniff(filter="icmp")
    ```
* step 2 - in a new window run 2 ping requests:
    ```
    anna@HP-Printer:~$ ping 127.0.0.1
    4 packets transmitted, 4 received, 0% packet loss, time 3058ms

    anna@HP-Printer:~$ ping google.com
    3 packets transmitted, 3 received, 0% packet loss, time 2003ms
    ```
* step 3 - show the summary of the sniffed packets in scapy:
    ```
    >>> a1.summary()
    Ether / IP / ICMP 10.6.1.195 > 216.58.204.46 echo-request 0 / Raw
    Ether / IP / ICMP 216.58.204.46 > 10.6.1.195 echo-reply 0 / Raw
    Ether / IP / ICMP 10.6.1.195 > 216.58.204.46 echo-request 0 / Raw
    Ether / IP / ICMP 216.58.204.46 > 10.6.1.195 echo-reply 0 / Raw
    ```
lets run another sniff, with interface filter:
* Step 1 - run in scapy:
    ```
    >>> a2 = sniff(filter="icmp",iface="lo")
    ```
* step 2 - in a new window run 2 ping requests:
    ```
    anna@HP-Printer:~$ ping 127.0.0.1
    4 packets transmitted, 4 received, 0% packet loss, time 3058ms

    anna@HP-Printer:~$ ping google.com
    3 packets transmitted, 3 received, 0% packet loss, time 2003ms
    ```
* step 3 - show the summary of the sniffed packets in scapy:
    ```
    a2.summary()
    Ether / IP / ICMP 127.0.0.1 > 127.0.0.1 echo-reply 0 / Raw
    Ether / IP / ICMP 127.0.0.1 > 127.0.0.1 echo-request 0 / Raw
    Ether / IP / ICMP 127.0.0.1 > 127.0.0.1 echo-request 0 / Raw
    Ether / IP / ICMP 127.0.0.1 > 127.0.0.1 echo-reply 0 / Raw
    Ether / IP / ICMP 127.0.0.1 > 127.0.0.1 echo-reply 0 / Raw
    ```



### prn
* `prn` - allows you to pass a function that executes with each packet sniffed.    
The intended purpose of this function is to control how the packet prints out in the console allowing you to replace the default packet printing display with a format of your choice.

The prn argument is defined as:
```
prn: function to apply to each packet. If something is returned, it is displayed. 
```
For instance you can use 
```
prn = lambda x: x.summary().
```

In order for your program/script to format and return the packet info as you wish, the sniff function passes the packet object as the one and only argument into the function you specify in the sniff’s prn argument. This gives us the option to do some stuff (not just formatting) with each packet sniffed 

For example, we can now perform custom actions with each sniffed packet. This can be anything from incrementing a packet count somewhere in the program, to doing some advanced packet parsing or manipulation, or even shipping that packet off into some sort of storage.

Here’s a simple example for keeping track of the number of packets sniffed
This script keeps a Counter with an A/Z pair of IP addresses, displays the total packet count with each packet print(), and then prints out the conversation counts at the end.



```python
from scapy.all import sniff

## Create a Packet Counter
packet_counts = 0

## Define our Custom Action function
def custom_action(packet):
    global packet_counts
    packet_counts +=1
    return f"Packet #{packet_counts}: {packet[0][1].src} ==> {packet[0][1].dst}"

## Setup sniff, filtering for IP traffic
sniff(filter="ip", prn=custom_action, count=10)

```
console output:
```
Packet #1: 10.6.2.79 ==> 10.6.15.255
Packet #2: 10.6.1.34 ==> 224.0.0.251
Packet #3: 216.58.206.46 ==> 10.6.1.195
Packet #4: 216.58.206.46 ==> 10.6.1.195
Packet #5: 216.58.206.46 ==> 10.6.1.195
Packet #6: 216.58.206.46 ==> 10.6.1.195
Packet #7: 10.6.1.195 ==> 216.58.206.46
Packet #8: 10.6.2.15 ==> 10.6.15.255
Packet #9: 216.58.206.46 ==> 10.6.1.195
Packet #10: 216.58.206.46 ==> 10.6.1.195
```

```python
from collections import Counter
from scapy.all import sniff

## Create a Packet Counter
packet_counts = Counter()

## Define our Custom Action function
def custom_action(packet):
    # Create tuple of Src/Dst in sorted order
    key = tuple(sorted([packet[0][1].src, packet[0][1].dst]))
    packet_counts.update([key])
    return f"Packet #{sum(packet_counts.values())}: {packet[0][1].src} ==> {packet[0][1].dst}"

## Setup sniff, filtering for IP traffic
sniff(filter="ip", prn=custom_action, count=10)

## Print out packet count per A <--> Z address pair
print("\n".join(f"{f'{key[0]} <--> {key[1]}'}: {count}" for key, count in packet_counts.items()))
```



Console Output:
```
Packet #1: 172.16.200.88 ==> 255.255.255.255
Packet #2: 172.16.200.88 ==> 172.16.98.255
Packet #3: 172.16.200.88 ==> 255.255.255.255
Packet #4: 172.16.200.88 ==> 255.255.255.255
Packet #5: 172.16.72.72 ==> 172.16.98.203
Packet #6: 172.16.98.203 ==> 172.16.72.72
Packet #7: 172.16.98.203 ==> 172.16.72.72
Packet #8: 172.16.72.72 ==> 172.16.98.203
Packet #9: 172.16.72.72 ==> 172.16.98.203
Packet #10: 172.16.98.203 ==> 172.16.72.72
172.16.200.88 <--> 255.255.255.255: 3
172.16.200.88 <--> 172.16.98.255: 1
172.16.72.72 <--> 172.16.98.203: 6
```

### Custom Formatted ARP Monitor
If we want to see all the `ARP` headers with scapy, we run in scapy shell:
```
>>> ls(ARP())
hwtype     : XShortField                         = 1               (1)
ptype      : XShortEnumField                     = 2048            (2048)
hwlen      : FieldLenField                       = None            (None)
plen       : FieldLenField                       = None            (None)
op         : ShortEnumField                      = 1               (1)
hwsrc      : MultipleTypeField                   = 'e4:70:b8:4b:f2:f3' (None)
psrc       : MultipleTypeField                   = '10.6.1.195'    (None)
hwdst      : MultipleTypeField                   = None            (None)
pdst       : MultipleTypeField                   = None            (None)

```
Here we use the same prn function and some conditional statements to very clearly tell us what ARP traffic our computer is seeing.

```python
from collections import Counter
from scapy.all import ARP, sniff

def arp_display(pkt):
    if pkt[ARP].op == 1: #who-has (request)
        return f"Request: {pkt[ARP].psrc} is asking about {pkt[ARP].pdst}"
    if pkt[ARP].op == 2: #is-at (response)
        return f"*Response: {pkt[ARP].hwsrc} has address {pkt[ARP].psrc}"

sniff(prn=arp_display, filter="arp", store=0, count=10)
```

Console Output:
```
Request: 172.16.20.168 is asking about 172.16.20.85
Request: 172.16.20.168 is asking about 172.16.20.229
Request: 172.16.20.2 is asking about 172.16.20.203
*Response: aa:bb:cc:29:a6:85 has address 172.16.20.203
Request: 172.16.20.200 is asking about 172.16.20.82
Request: 172.16.20.51 is asking about 172.16.20.254
Request: 172.16.20.15 is asking about 172.16.20.58
Request: 172.16.20.15 is asking about 172.16.20.58
Request: 172.16.20.200 is asking about 172.16.20.44
*Response: dd:ee:ff:a2:02:bf has address 172.16.20.44
```
#### Note
An important thing to keep in mind when using the prn argument
In the case of the example above, you are passing the custom_action function into the sniff function. If you used  sniff(prn=custom_action()) instead, you would be passing the function’s returned value to the sniff function. This will generate the returned text before the function has a packet to parse and will not give you the results you want.



#### Using nested functions

Using nested functions to harness the power of closure, you can bind any number of arguments to the function that is executed on each packet by Scapy. 
In order to bind additional arguments to the prn function, we have to use nested functions.

```python
from scapy.all import sniff


# create parent function with passed in arguments
def custom_action(start_line, end_line):

  def print_packet(p):
    return f"{start_line} {p[0][1].src} {end_line}"

  return print_packet

sniff(filter="ip", prn=custom_action("**" , "$$" ), count=5)
```



Here’s an order-of-events explanation for what’s happening:

We define our url & token variables, just like in the first example.
We define the custom_action function. This will be run when the scapy sniff function first runs to get the value info for the prn argument. Note the two parameters that we pass into custom_action.
Inside custom_action, we create another function that takes the scapy implicitly passed packet as a parameter. This is the function that will upload the packet info to our API.
The upload_packet function is nested in custom_action so it has access to the url & token variables because it is inside the parent function’s scope.
The return value of custom_action is the upload_packet function, so this function will be run along with every sniffed packet based on the prn argument. Even though the custom_action function is not executed to take in the url & token parameters, they are locked into the nested upload_packet function due to Python’s capacity for ‘closure’.
After we define the custom_action and nested upload_packet functions, we run the Scapy sniff function with the returned value of custom_action passed via the prn argument.
Using closures to ‘lock-in’ any number of arguments to the custom_action function gives us much more flexibility.




_________________________________

* `stop_filter` - Python function applied to each packet to determine if
                we have to stop the capture after this packet.
                --Ex: stop_filter = lambda x: x.haslayer(TCP)
* `monitor` use monitor mode. May not be available on all OS
* `started_callback` - called as soon as the sniffer starts sniffing (default: None).
* `L2socket`  - use the provided L2socket (default: use conf.L2listen).
* `opened_socket` provide an object (or a list of objects) ready to use .recv() on.
Examples:
sniff(iface="eth0", prn=Packet.summary)
sniff(iface=["eth0", "mon0"],prn=lambda pkt: "%s: %s" % (pkt.sniffed_on, pkt.summary()))
sniff(iface={"eth0": "Ethernet", "mon0": "Wifi"}, prn=lambda pkt: "%s: %s" % (pkt.sniffed_on,pkt.summary()))