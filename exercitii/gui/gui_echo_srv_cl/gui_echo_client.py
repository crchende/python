#!/usr/bin/env python3
# cip_chende@yahoo.com

from lib.txt_for_chat import ChatWindow

from socket import *
import time

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 7000        # The port used by the server
ADDR = (HOST, PORT)

#MAXMSG = 10

s = socket(AF_INET, SOCK_STREAM)
s.connect(ADDR)
     
cw = ChatWindow(s)
cw.mw.mainloop()    
    
s.close()
print("Client socket closed")

