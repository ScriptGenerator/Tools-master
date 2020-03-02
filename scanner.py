import socket, sys
from threading import Thread
open_ports = []
ip = sys.argv[1]
def scan(from_port,to_port) :
	i = int(to_port) - int(from_port)
	for port in range(i):
		try :
			s = socket.socket()
			s.settimeout(2)
			s.connect(( str(ip) , ( int(from_port) + port ) ))
			open_ports.append(str(port + int(from_port)))
		except socket.timeout :
			s.shutdown(socket.SHUT_RDWR)
			s.close()
def clear_threads(t):
	x = int(t) - 10
	while 1:
		if x == -10 :
			break
		cmds = "t{0}.join()".format(str(x))
		exec(cmds.format(str(x)))
		x -= 10
if __name__ == '__main__':
	i4 = 0
	while 1:
		if i4 == 10000 or i4 == 20000 or i4 == 30000 or i4 == 40000 or i4 == 50000 or i4 == 60000:
			clear_threads(i4)
		if i4 == 65500:
			break
		command = "t{0} = Thread(target=scan,args=({1},{2}))".format(str(i4),str(i4),str(i4 + 10))
		#print("starting :",command)
		exec(command)
		command2 = "t{0}.start()".format(str(i4))
		exec(command2)
		i4 += 10
	print("open ports :")
	for item in open_ports:
		print("    ",item,)
	print("cleaning up for quitting ...")
	exit()