#!/usr/bin/python3

import binascii
import socket
import struct

ICMP_ECHO_REQUEST = 8 # Platform specific

# see https://tools.ietf.org/html/rfc1624
def checksum(data):
    sum = 0
    max_count = (len(data)/2)*2
    count = 0
    while count < max_count:
        val = data[count + 1]*256 + data[count]            
        sum = sum + val
        sum = sum & 0xffffffff 
        count = count + 2
    
    if max_count<len(data):
        sum = sum + ord(data[len(data) - 1])
        sum = sum & 0xffffffff 
    
    sum = (sum >> 16)  +  (sum & 0xffff)
    sum = sum + (sum >> 16)
    answer = ~sum
    answer = answer & 0xffff
    answer = answer >> 8 | (answer << 8 & 0xff00)
    return answer


#def send_ping():

#def receive_pong():
# https://github.com/PacktPublishing/Python-Network-Programming-Cookbook-Second-Edition/blob/master/Chapter03/3_2_ping_remote_host.py

icmp_protocol = socket.getprotobyname('icmp')  # see /etc/protocols
target_host = socket.gethostbyname('www.seznam.cz')
packet_id = 1234

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp_protocol)
    my_checksum = 0
    
    # Create a dummy header with a 0 checksum.
    header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, my_checksum, packet_id, 1)
    data = b'12345678'

    # Get the checksum on the data and the dummy header and put it into the header
    my_checksum = checksum(header + data)
    header = struct.pack(
        "bbHHh", ICMP_ECHO_REQUEST, 0, socket.htons(my_checksum), packet_id, 1
    )
    packet = header + data
    s.sendto(packet, (target_host, 1))
    s.close()
except Exception as e:
    print('ERROR: ' + str(e))

