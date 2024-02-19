#!/usr/bin/env python3
# cip_chende@yahoo.com

import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 7000    The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    
    try:
        while True:
            data = input("Tastati ceva: ");
            print(" Trimit -> ", data.encode())
            s.sendall(data.encode()) # conversie str -> bytes, pt a putea transmite pe socket
            print(" Primit <-: ")
            data = s.recv(1024)
            print(repr(data))
    except KeyboardInterrupt:
        print(" ... caught keyboard interrupt, exiting")
    
    #finally:
   s.close()
not needed, with will take care of closign the socket
        

