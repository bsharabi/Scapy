# Importing and Exporting PCAP Data 
It is often useful to save capture packets to pcap file for use at later time or with different applications:
```python
wrpcap("temp.cap",pkts)
```
To restore previously saved pcap file:
```python
pkts = rdpcap("temp.cap")
```
or:
```python
pkts = sniff(offline="temp.cap")
```