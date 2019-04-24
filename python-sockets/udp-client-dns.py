#!/usr/bin/python3

import binascii
import socket
import struct

message_id = 12345
options = 0x0100

dns_header = struct.pack('!HHHHHH', message_id, options, 1, 0, 0, 0)
dns_question = struct.pack('!B3sB3sB2sBHH', 3, b'www', 3, b'zcu', 2, b'cz', 0, 1, 1)

message = dns_header + dns_question

server_address = ('8.8.8.8', 53)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    sock.sendto(message, server_address)
    response, _ = sock.recvfrom(4096)
finally:
    sock.close()

last_field = response[-4:]
(n1, n2, n3, n4) = struct.unpack('!BBBB', last_field)
print(str(n1) + '.' + str(n2) + '.' + str(n3) + '.' + str(n4))

with open('response.bin', 'wb') as file:  # Use file to refer to the file object
    file.write(response)


    #                                 1  1  1  1  1  1
    #   0  1  2  3  4  5  6  7  8  9  0  1  2  3  4  5
    # +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    # |                      ID                       |
    # +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    # |QR|   Opcode  |AA|TC|RD|RA|   Z    |   RCODE   |
    # +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    # |                    QDCOUNT                    |
    # +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    # |                    ANCOUNT                    |
    # +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    # |                    NSCOUNT                    |
    # +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    # |                    ARCOUNT                    |
    # +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+

# scapy: sr1(IP(dst="8.8.8.8")/UDP()/DNS(rd=1,qd=DNSQR(qname="www.zcu.cz")))