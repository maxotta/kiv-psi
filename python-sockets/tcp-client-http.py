#!/usr/bin/python3

from socket import *

s = socket(AF_INET, SOCK_STREAM) # IPv4, TCP

s.connect(('www.root.cz', 80)) # Connect (host, port)

s.send(b'GET / HTTP/1.0\n\n') # Send request

data = s.recv(10000) # Get response
print('Response: ' + str(data))

s.close()
