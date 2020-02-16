import scapy.all as scapy
from scapy_http import http
import subprocess
interface=input("enter interface:")
def listenstart(interface):
    print("listener start[OK!]")
    scapy.sniff(iface=interface,store=False,prn=sniffer)
    print("shutdown[OK!]")
def sniffer(packets):
    if packets.haslayer(http.HTTPRequest):
        if packets.haslayer(scapy.Raw):
            print(packets[scapy.Raw].load)
listenstart(interface)