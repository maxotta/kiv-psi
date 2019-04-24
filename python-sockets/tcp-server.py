#!/usr/bin/python3
# 147.228.131.64
from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(('127.0.0.1', 8080))
s.listen(0)
while True:
    c,a = s.accept()
    print("Received connection from " + str(a))
    c.send(("Hello " + str(a[0]) + "\n").encode())
    c.close()

