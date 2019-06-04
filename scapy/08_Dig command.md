
# Dig
```
anna@HP-Printer:~$ whatis dig
dig (1)              - DNS lookup utility
```
Dig command gets an address and returns the ip address, but we can use the `-x` option that stands for Simplified reverse lookups, for mapping addresses to names.   


Simple usage of the dig command:
```
anna@HP-Printer:~$ dig -x 8.8.4.4 +short
google-public-dns-b.google.com.

anna@HP-Printer:~$ dig google.com +short
172.217.21.206
```


#### Ping VS Hostconf
```
anna@HP-Printer:~$ whatis ping
ping (8)             - send ICMP ECHO_REQUEST to network hosts
anna@HP-Printer:~$ whatis host
host (1)             - DNS lookup utility
```
* Ping is in order to check troubles in the network
* Host - doesnt send a ping (only DNS request)
```
anna@HP-Printer:~/Desktop/scapy-2019B-II$ ping google.com
PING google.com (172.217.18.110) 56(84) bytes of data.

anna@HP-Printer:~/Desktop/scapy-2019B-II$ host google.com
google.com has address 172.217.18.110

```

#### Get the used domain in our computer
* Run the following command: (the `nameserver` address - is the DNS address)

```
anna@HP-Printer:/$ cat /etc/resolv.conf
# This file is managed by man:systemd-resolved(8). Do not edit.
#
# This is a dynamic resolv.conf file for connecting local clients to the
# internal DNS stub resolver of systemd-resolved. This file lists all
# configured search domains.
#
# Run "systemd-resolve --status" to see details about the uplink DNS servers
# currently in use.
#
# Third party programs must not access this file directly, but only through the
# symlink at /etc/resolv.conf. To manage man:resolv.conf(5) in a different way,
# replace this symlink by a static file or a different symlink.
#
# See man:systemd-resolved.service(8) for details about the supported modes of
# operation for /etc/resolv.conf.

nameserver 127.0.0.53
options edns0
```
* We can see this address in use (`SERVER: 127.0.0.53`), when we run dig command:
```
anna@HP-Printer:/$ dig google.com

; <<>> DiG 9.11.3-1ubuntu1.5-Ubuntu <<>> google.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 38181
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 65494
;; QUESTION SECTION:
;google.com.			IN	A

;; ANSWER SECTION:
google.com.		88	IN	A	172.217.18.174

;; Query time: 251 msec
;; SERVER: 127.0.0.53#53(127.0.0.53)
;; WHEN: Fri Mar 22 17:05:53 IST 2019
;; MSG SIZE  rcvd: 55
```
* Lets change the DNS in `/etc/resolv.conf` (only for this runtime)
```
anna@HP-Printer:/$ sudo nano /etc/resolv.conf
```

when the nano window opens - comment out (with `#`) the line:
```
nameserver 127.0.0.53
```
and press `ctrl+X` to exit nano

Now if we try to run a `dig` command, we will recive that no servers could be reached:
```
anna@HP-Printer:/$ dig google.com
; <<>> DiG 9.11.3-1ubuntu1.5-Ubuntu <<>> google.com
;; global options: +cmd
;; connection timed out; no servers could be reached
```

Now run again:
```
anna@HP-Printer:/$ sudo nano /etc/resolv.conf
```

when the nano window opens - change the line:
```
#nameserver 127.0.0.53
```

to:
```
nameserver 1.1.1.1  
```

now when we run the `dig` command we will success and see the new address that we configured:
```
anna@HP-Printer:/$ dig google.com

; <<>> DiG 9.11.3-1ubuntu1.5-Ubuntu <<>> google.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 8524
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1452
;; QUESTION SECTION:
;google.com.			IN	A

;; ANSWER SECTION:
google.com.		284	IN	A	172.217.22.14

;; Query time: 93 msec
;; SERVER: 1.1.1.1#53(1.1.1.1)
;; WHEN: Fri Mar 22 17:16:41 IST 2019
;; MSG SIZE  rcvd: 55
```

#### Run dig with different DNS record types
Resource records are the data type that is being saved inside the DNSs,
for example:

* `A` - IPv4 Record
* `AAAA`- IPv6 Record
* `MX` - Mail eXchange record that Maps a domain name to a list of message transfer agents for that domain


We can use this record types with the command `dig`:
* To get an IPv4 address: (default)
```
anna@HP-Printer:/$ dig google.com

; <<>> DiG 9.11.3-1ubuntu1.5-Ubuntu <<>> google.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 51037
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1452
;; QUESTION SECTION:
;google.com.			IN	A

;; ANSWER SECTION:
google.com.		4	IN	A	172.217.22.14

;; Query time: 141 msec
;; SERVER: 1.1.1.1#53(1.1.1.1)
;; WHEN: Fri Mar 22 17:21:21 IST 2019
;; MSG SIZE  rcvd: 55

```
* To get an IPv6:
```
anna@HP-Printer:/$ dig AAAA google.com

; <<>> DiG 9.11.3-1ubuntu1.5-Ubuntu <<>> AAAA google.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 27747
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1452
;; QUESTION SECTION:
;google.com.			IN	AAAA

;; ANSWER SECTION:
google.com.		175	IN	AAAA	2a00:1450:4001:81a::200e

;; Query time: 71 msec
;; SERVER: 1.1.1.1#53(1.1.1.1)
;; WHEN: Fri Mar 22 17:20:06 IST 2019
;; MSG SIZE  rcvd: 67
```
* To get the Mail exchange IPs:
```
anna@HP-Printer:~$ dig MX google.com

; <<>> DiG 9.11.3-1ubuntu1.5-Ubuntu <<>> MX google.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 62550
;; flags: qr rd ra; QUERY: 1, ANSWER: 5, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1452
;; QUESTION SECTION:
;google.com.			IN	MX

;; ANSWER SECTION:
google.com.		291	IN	MX	10 aspmx.l.google.com.
google.com.		291	IN	MX	20 alt1.aspmx.l.google.com.
google.com.		291	IN	MX	30 alt2.aspmx.l.google.com.
google.com.		291	IN	MX	40 alt3.aspmx.l.google.com.
google.com.		291	IN	MX	50 alt4.aspmx.l.google.com.

;; Query time: 121 msec
;; SERVER: 1.1.1.1#53(1.1.1.1)
;; WHEN: Fri Mar 22 17:28:43 IST 2019
;; MSG SIZE  rcvd: 147
```


### Authoritative name server
An authoritative name server is a name server that only gives answers to DNS queries from data that has been configured by an original source, for example, the domain administrator or by dynamic DNS methods, in contrast to answers obtained via a query to another name server that only maintains a cache of data.

An authoritative name server can either be a master server or a slave server.    
* A master server is a server that stores the original (master) copies of all zone records. 
* A slave server uses a special automatic updating mechanism in the DNS protocol in communication with its master to maintain an identical copy of the master records.

Every DNS zone must be assigned a set of authoritative name servers. This set of servers is stored in the parent domain zone with name server (NS) records.

An authoritative server indicates its status of supplying definitive answers, deemed authoritative, by setting a protocol flag, called the "Authoritative Answer" (AA) bit in its responses.

This flag is usually reproduced prominently in the output of DNS administration query tools, such as dig, to indicate that the responding name server is an authority for the domain name in question.

#### For example:
We will use `NS` - Name server record - Delegates a DNS zone to use the given authoritative name servers

```
anna@HP-Printer:~$ dig NS ynet.co.il

; <<>> DiG 9.11.3-1ubuntu1.5-Ubuntu <<>> NS ynet.co.il
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 1762
;; flags: qr rd ra; QUERY: 1, ANSWER: 8, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1452
;; QUESTION SECTION:
;ynet.co.il.			IN	NS

;; ANSWER SECTION:
ynet.co.il.		289	IN	NS	ns1-92.akam.net.
ynet.co.il.		289	IN	NS	ns1-168.akam.net.
ynet.co.il.		289	IN	NS	eur2.akam.net.
ynet.co.il.		289	IN	NS	usc2.akam.net.
ynet.co.il.		289	IN	NS	use1.akam.net.
ynet.co.il.		289	IN	NS	usw1.akam.net.
ynet.co.il.		289	IN	NS	asia2.akam.net.
ynet.co.il.		289	IN	NS	ns1-61.akam.net.

;; Query time: 296 msec
;; SERVER: 1.1.1.1#53(1.1.1.1)
;; WHEN: Fri Mar 22 17:48:34 IST 2019
;; MSG SIZE  rcvd: 207
```

Then we will use the first NS to direct dig request: 
```
anna@HP-Printer:~$ dig NS ynet.co.il @ns1-92.akam.net.

; <<>> DiG 9.11.3-1ubuntu1.5-Ubuntu <<>> NS ynet.co.il @ns1-92.akam.net.
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 42247
;; flags: qr aa rd; QUERY: 1, ANSWER: 8, AUTHORITY: 0, ADDITIONAL: 1
;; WARNING: recursion requested but not available

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
;; QUESTION SECTION:
;ynet.co.il.			IN	NS

;; ANSWER SECTION:
ynet.co.il.		300	IN	NS	ns1-168.akam.net.
ynet.co.il.		300	IN	NS	usw1.akam.net.
ynet.co.il.		300	IN	NS	eur2.akam.net.
ynet.co.il.		300	IN	NS	use1.akam.net.
ynet.co.il.		300	IN	NS	ns1-61.akam.net.
ynet.co.il.		300	IN	NS	usc2.akam.net.
ynet.co.il.		300	IN	NS	ns1-92.akam.net.
ynet.co.il.		300	IN	NS	asia2.akam.net.

;; Query time: 366 msec
;; SERVER: 193.108.91.92#53(193.108.91.92)
;; WHEN: Fri Mar 22 17:49:10 IST 2019
;; MSG SIZE  rcvd: 207
```

You can see that in the first dig we got:
```
;; flags: qr rd ra; QUERY: 1, ANSWER: 8, AUTHORITY: 0, ADDITIONAL: 1
```
and in the second dig we got:
```
;; flags: qr aa rd; QUERY: 1, ANSWER: 8, AUTHORITY: 0, ADDITIONAL: 1
```
with the `aa` flag that stands for "Authoritative Answer".


#### Run dig for all types
```
anna@HP-Printer:~$ dig google.com any +noall +answer

; <<>> DiG 9.11.3-1ubuntu1.5-Ubuntu <<>> google.com any +noall +answer
;; global options: +cmd
google.com.		299	IN	A	172.217.16.142
google.com.		299	IN	AAAA	2a00:1450:4001:808::200e
google.com.		299	IN	TXT	"docusign=05958488-4752-4ef2-95eb-aa7ba8a3bd0e"
google.com.		21599	IN	NS	ns2.google.com.
google.com.		21599	IN	NS	ns3.google.com.
google.com.		599	IN	MX	30 alt2.aspmx.l.google.com.
google.com.		3599	IN	TXT	"facebook-domain-verification=22rm551cu4k0ab0bxsw536tlds4h95"
google.com.		59	IN	SOA	ns1.google.com. dns-admin.google.com. 238640061 900 900 1800 60
google.com.		21599	IN	NS	ns1.google.com.
google.com.		3599	IN	TXT	"globalsign-smime-dv=CDYX+XFHUw2wml6/Gb8+59BsH31KzUr6c1l2BPvqKX8="
google.com.		3599	IN	TXT	"v=spf1 include:_spf.google.com ~all"
google.com.		599	IN	MX	40 alt3.aspmx.l.google.com.
google.com.		21599	IN	NS	ns4.google.com.
google.com.		21599	IN	CAA	0 issue "pki.goog"
google.com.		599	IN	MX	10 aspmx.l.google.com.
google.com.		599	IN	MX	20 alt1.aspmx.l.google.com.
google.com.		599	IN	MX	50 alt4.aspmx.l.google.com.
```
