# scapy-2019B-II

### Part 0 - introduction to scapy
* What is apt
* What is pip 
* 2 ways to run scapy
    * via python script (with `import` to scapy)
    * via `scapy terminal`
* layer of `Ethernet` and `Bluetooth` in OSI Model (second layer)
* layer of `ip` in OSI Model (third layer)
* layer of `UDP` and `TCP` in OSI Model (fourth layer)

### Part 1 - get protocol headers, packet info, and send packets
* How to show all the properties of a specific packet (`ls()`,`show()`)
* in `IP` you need to know how to set: `src`, `dst`
* create a new `IP` for a packet

### Part 2 - ICMP (ping)
* What is ICMP
* How to send an `ICMP` packet to specific ip address, and get the response


### Part 3 - Send UDP packet
* Build a `TCP` or `UDP` packet (the base of this packet is `IP`)
* in `UDP` you need to know how to set: `dport`, `sport`

### Part 4 - DNS
* Whats is DNS
* What is `dig` command in linux
* How to send a DNS  request with scapy

### Part 5 - sniff
* What is `tcpdump` command in linux
* what is the `sniff` function 
    * `summary` - shows the summary of all the sniffed packets
    * aceess specific packet from the sniffed packets (with the packet index)
    * Resend a snoiffed packet (with `sendp`) after changing the packet values
* write sniffed packets to `pacap` file with scapy
* 2 ways to read packets from `pacap` file with scapy 
    * `rdcap("")`
    * `sniff(offline="")`
* sniff options (`prn`, `count`, etc...)
