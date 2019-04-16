from scapy.all import *

# a=$(netstat -i | tail -n$[ $(netstat -i | wc -l)-2] | cut -d' ' -f1)
# ip a
# netstat -i 

lo= sniff(filter="ip",iface="lo",count=30,timeout=3)
enp0s3= sniff(filter="ip",iface="enp0s3",count=30,timeout=3)
lo.show()
enp0s3.show()
print(lo)
print(enp0s3)