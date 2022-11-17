#import socket module

import socket

s = socket.socket()
port = 40674
s.connect(('127.0.0.1', port))
print(s.recv(1024))#size of the data(1040 byte)

s.close()