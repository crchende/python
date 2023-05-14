#!/usr/bin/env python3
# cip_chende@yahoo.com

# example on net: https://gist.github.com/micktwomey/606178

# Multithreading server

from socket import *

import multiprocessing
import time

# In previus examples echoX - it was used print to print messages.
# A 
# using logging for the messages that describe the functionality ...
import logging

# instead of print("debug / info message")
# will use logging.debug / logging.info messages
# these messages will also be formatted by logger module

#Using basic config - this is for the root logger
#our logger is a child of root logger so it will inherit the root logger settings
logging.basicConfig(level = logging.DEBUG)




#############
# 1) Creating the thread wiht threading.Thread
#    running it with t1.start()
#############
'''
t1 = threading.Thread(target = func_to_run_in_thread, args=("t1  ",))
t1.start()

process = mulhttps://gist.github.com/micktwomey/606178tiprocessing.Process(target=handle, args=(conn, address))
process.daemon = True
'''

def handle_client_connection(connection, address, connection_count):
    # this will be executed in a new process
    # should import here whatever is needed in the new process
    #???
    
    logc = logging.getLogger("process %r" % (address[1],))
     
    #Re
    logc.debug("Accepted connection from address: {}. Start sending; Sending & receiving data".format(address))
        
    with connection:
        while True:
            data = connection.recv(1024)
            if not data:
                break
            logc.debug("Received data: '{}' and seding it back to client {}".format(data.decode('ascii'), address[1]))
            connection.sendall(data)

    logc.debug("Client connection {} from port: {} ended".format(connection_count, address[1]))


HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 7000        # Port to listen on (non-privileged ports are > 1023)

s = socket(AF_INET, SOCK_STREAM)
#s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) # this is needed for multthreading but not for multiprocess
s.bind((HOST, PORT))

logs = logging.getLogger("Server")


s.listen(1) # listen but allow no more than 2 pending connections
logs.info("Server started. It is listening on: {}.{}".format(HOST, PORT))
logs.info(" - waiting for connections - accept call")

i = 1
try:
    while 1:
        conn, addr = s.accept()
        logs.debug("Accepted connection from: {}:{}".format(addr[0], addr[1]))
        p = multiprocessing.Process(target = handle_client_connection, args=(conn, addr, i))
        p.daemon = True
        p.start()
        i += 1
except KeyboardInterrupt:
    logs.info(" ... caught keyboard interrupt. Exiting ...")
    
finally:
    logs.debug("Closing the server socket")
    s.close()
    logs.debug("Server socket closed")

