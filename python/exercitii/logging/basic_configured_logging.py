#!/usr/bin/env python3

# using default logging
# 'root' logger is used
# warning level - all log messages under warning are not shown 

# basic configuration using basicConfig

import logging

#logging.basicConfig(level = logging.DEBUG)

#the second call of basicConfig does nothing. It can be called only once.
#logging.basicConfig(format="%(levelname)s%(message)s")


'''
 Folosim root logger.
 Functia logging.basicConfig() trebuie apelata la inceputul programului.
 Al doilea apel al functiei nu mai are nici un efect.
 
 Timpul inclus in mesajul logat, poate fi formatata cu ajutorul parametrului datefmt.
 
 
'''

logging.basicConfig(format="%(asctime)s %(module)s %(name)s %(levelname)s: %(message)s",
    filename = __name__ + ".log",
    level=logging.DEBUG, 
    datefmt="%Y-%m-%d %H:%M:%S")

logging.debug('log msg - debug')
logging.info('log msg - info')
logging.warning('log msg - warning')
logging.error('log msg - error')
logging.critical('log msg - critical')
