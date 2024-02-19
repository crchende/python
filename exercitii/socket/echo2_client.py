#!/usr/bin/env python3
# cip_chende@yahoo.com

from socket import *
import time

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 7000    The port used by the server
ADDR = (HOST, PORT)

MAXMSG = 10

s = socket(AF_INET, SOCK_STREAM)
s.connect(ADDR)

i = 1
while i < MAXMSG:
    msg = "Hello world - " + str(i)
    b_msg = msg.encode('ascii')
    #s.sendall(b'Hello, world')
    s.sendall(b_msg)
    data = s.recv(1024)
    print('Received - binary', data, " - and ascii decoded: ", data.decode('ascii'))
    i += 1
    time.sleep(1)
    
s.close()
print("Client socket closed")

