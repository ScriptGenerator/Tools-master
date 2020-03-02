from scapy.all import *
import requests
import pprint
import codecs
import json
import sys
import shutil
from threading import Thread
import time
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

ip_mac_dic = {}
rangeofips = 256

def scan_network(type_ip,From,to):
	i = int(From)
	while i < int(to) :
		if i == 0:
			continue
		ip  = str(type_ip) + str(i)
		if i == 100:
			print("100 ip cheked")
		if i == 200:
			print("almost done ..")
		try :
			ans, unans = srp(Ether(dst = "ff:ff:ff:ff:ff:ff")/ARP(pdst=ip),timeout=1, iface = 'wlo1',inter=1,verbose=0)
			target_m = ans[0][1].hwsrc
			target_m = str(target_m)
			ip_mac_dic[ip] = target_m
		except IndexError :
			pass
		i = i + 1
def nscan_network(type_ip,f_o):
	ip  = str(type_ip) + str(f_o)
	try :
		ans, unans = srp(Ether(dst = "ff:ff:ff:ff:ff:ff")/ARP(pdst=ip),timeout=1, iface = 'wlo1',inter=1,verbose=0)
		target_m = ans[0][1].hwsrc
		target_m = str(target_m)
		ip_mac_dic[ip] = target_m
	except IndexError :
		pass
	
def get_info(mac):
	MAC_URL = 'http://macvendors.co/api/%s'
	r = requests.get(MAC_URL % str(mac))
	info = r.json()
	r.close()
	info = info['result']
	s_hex = info['start_hex']
	company = info['company']
	address = info['address']
	mac_prefix = info['mac_prefix']
	country = info['country']
	type_m = info['type']
	end_hex = info['end_hex']
	return s_hex, company, address, mac_prefix, country, type_m, end_hex
columns = shutil.get_terminal_size().columns
def rapport(ip_addr,mac_addr):
	print("\n\n")
	ip_r = bcolors.OKGREEN + str(ip_addr) + bcolors.ENDC
	intro = "Gudom result repport for " + ip_r + " :"
	print(intro.center(columns))
	#start_hex, company, address, mac_prefix, country, type_m, end_hex = get_info(str(mac_addr))
	f = """
	  +----------------------------------------------------------------------------------------------------------
	 /									   
	|		   	{0} : {1}                     
	|
	|		   	{2} : {3}
	|
	|		   	{4} : {5}
	|
	|		   	{6} : {7}
	|
	|		   	{8} : {9}
	|
	|			{10} : {11}
	|
	|			{12} : {13}
	|
	|			{14} : {15}
	+
	 \___________________________________________________________________________________________________________
	

	"""
	s_hex, company, address, mac_prefix, country, type_m, end_hex = get_info(mac_addr)
	print(bcolors.BOLD + f.format("MAC ADDRESS",mac_addr,"Start hex",s_hex,"End hex",end_hex,"MAC prefix",mac_prefix,"Company",company,"Country",country,"Address",address,"type",type_m) + bcolors.ENDC)

if __name__ == '__main__':
	print("\n")
	logo = bcolors.OKBLUE + "Starting GUDOM (https://github.com/ScriptGenerator/ip-tools) at {0}".format(time.ctime()) + bcolors.ENDC
	print(logo.center(columns))
	print("\n")
	for g in range(256):
		if g == 0:
			continue
		f = "t{0} = Thread(target=nscan_network, args=('192.168.0.',{1}))".format(str(g),str(g))
		exec(f)
	for s in range(256):
		if s == 0:
			continue
		statement = "t{0}.start()".format(str(s))
		exec(statement)
	t1.join()
	for j in range(256):
		if j == 0:
			continue
		join_k = "t{0}.join()".format(str(j))
		exec(join_k)
	print(bcolors.FAIL + "We got the following informations by a cool API called macvendors." + bcolors.ENDC)
	for key, value in ip_mac_dic.items() :
	    print('')
	    rapport(key,value)
	    time.sleep(2)
	    print("\n\n")
