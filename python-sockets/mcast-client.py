#!/usr/bin/python3

import socket

MCAST_GRP = '224.0.0.99'
MCAST_PORT = 5007

msg = 'Hello Dolly'

# Set up UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
s.settimeout(2)
s.sendto(msg.encode(), (MCAST_GRP, MCAST_PORT) )

try:
    while True:
        data, addr = s.recvfrom(65507)
        print('RESPONSE FROM:' + str(addr))
        print('DATA: ' + data.decode())
except socket.timeout:
    pass
