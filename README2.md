# ip-tools
Ip tools is a series of ip tools that i programmed in python , i developed these tools for my networking/programing education
and im not responsable about ANYTHING you do with these scripts
# Tool number 1 : GET HIM OUT
get_his_ass_out.py is a very powerfull internal network dos [denial of service] attack tool which is programmed in python 3 that uses
the scapy library to detect mac addresses and their ips from the internal network and DOS them. the script is using a new technique to dos internal clients.
# How is that possible
Well basically it work pretty much like man in the middle attack (or arp-cache poisoning) but without
port forwarding ...
First of all we send ARP packets continiousely and with high speed to the target telling him that we are the new getaway and
he will memorize that in his arp-cache. Thereafter when the target wanna reach a certain server he will end up
with sending requests to us because he think that we are the getaway.
So what we can do about it ? 
well to make sure that the getaway don't recognize any changes we must to let it think that the target is still up (connect) and how we're gona do that ?... easy peassy just by sending ARP packets pretending that we are the target. I'm actually surprised with how little code I needed to write to perform such attack. this is due to the sipmlicity of the chosen programming language and API.  
# Butt isn't that arp-cache poisoning attack ?
No, because we are not using port forwarding here. Arp-cache poisoning is mainly used to watch the incoming/outgoing trafic on a certain clients, and you can forbid the client from reaching certain destinations. However, in this situation we are doing full dos.
# Tool number 2 : GUDOM
Gudom  is a tool that discover the network using ARP broadcasting then we investigate the ARP packets that have been received and extract the mac addresses in them then we request an open API which gonna tell us everything about the mac adresses that we got.
# installation
You just need python3 and scapy3

scapy repository : https://github.com/phaethon/scapy

python weebsite : https://python.org/
