import socket
import subprocess
import sys

from datetime import datetime

subprocess.call('clear',shell=True)

remoteServer =input("Enter a remote host to scan:")
remoteServer = socket.gethostbyname(remoteServer)

print("_" * 60)
print("Please wait ,scanning remote host", remoteServer)
print("_" *60)

#check the data and time  the scan was started
t1 = datetime.now()
#also we will do error handling

try:
	for port in range (15000):
		socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		result = sock.connect_ex((remoteServerIP, port))
		if result ==0:
			print("Port {}:		open".format(port))
			sock.close()
			
except KeyboardInterrupt:
	print("You pressed Ctrl+C")
	sys.exit()
	
except socket.gaierror:
	print("Hostname could not be resolved. Exiting")
	sys.exit()

except socket.error:
	print("Couldn't connect to server")
	sys.exit()