#!/usr/bin/env python3
# cip_chende@yahoo.com

# Multithreading server
# Use it with echo2_client.py
# You can start many terinals and run in paralel the client in each terminal
# This should work without problems
#
# PROBLEM - possible DoS atack - startint too many clients in paralels ...
#
# Other approach - used dedicated classes as ThreadingUDPServer or ThreadingTCPServer
#
# This example uses the low level components to show the basic "mechanic" in a simple example 

from socket import *

import threading
import time


#############
# 1) Creating the thread wiht threading.Thread
#    running it with t1.start()
#############
'''
t1 = threading.Thread(target = func_to_run_in_thread, args=("t1  ",))
t1.start()
'''

def handle_client_connection(connection, address, connection_count):
    print("Accepted connection from address: {}. Start sending; Sending & receiving data".format(address))
        
    with connection:
        while True:
            data = connection.recv(1024)
            if not data:
                break
            confirm_msg = "(Port: " + str(address[1]) + ") " + data.decode('ascii')
            print("Received data:", data.decode('ascii'), "Sending confirmation:", confirm_msg)
            
            b_c_msg = confirm_msg.encode('ascii')
            connection.sendall(b_c_msg)

    print("Client connection {} from port: {} ended".format(connection_count, address[1]))


HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 7000        # Port to listen on (non-privileged ports are > 1023)

s = socket(AF_INET, SOCK_STREAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind((HOST, PORT))

s.listen(1) # listen but allow no more than 2 pending connections
print("Server started. It is listening on: {}.{}".format(HOST, PORT))
print(" - waiting for connections - accept call")

i = 1
try:
    while 1:
        conn, addr = s.accept()
        t = threading.Thread(target = handle_client_connection, args=(conn, addr, i))
        t.start()
        i += 1
except KeyboardInterrupt:
    print(" ... caught keyboard interrupt. Exiting ...")
    
finally:
    print("\nClosing the server socket")
    s.close()
    print("Server socket closed")

