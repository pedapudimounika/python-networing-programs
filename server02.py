import socket

s = socket.socket()
print("Socket successfully created")

port = 40674 #0-1200 port is reserved for system 

s.bind(('', port)) # '' : IP address open : take request from any machin in the network , bind() -->2 params:
print("socket binded to %s" %(port))

s.listen(5)

print("socket is listening")

while True:
	c, addr = s.accept()
	c.send(b'Thank you for connecting')
	c.close()