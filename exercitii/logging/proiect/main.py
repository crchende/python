import logging

print()

#create logger 
logger = logging.getLogger("lproj") 
logger.setLevel(logging.DEBUG) 

# create console handler and set 
# level to debug 
ch = logging.StreamHandler() 
ch.setLevel(logging.DEBUG)

fh = logging.FileHandler('CipCode/logs.py')
fh.setLevel(logging.DEBUG)

# create formatter 
formatter = logging.Formatter\
('%(asctime)s.%(msecs)03d - %(levelname)s - %(name)s - module: %(module)s	- func: %(funcName)s	- line: %(lineno)s 	- %(message)s',
	datefmt = "%Y-%m-%d %H:%M:%S") 
	
#('%(asctime)s.%(msecs)03d - %(levelname)s - %(name)s - module: %(module)s - func: %(funcName)s - line: %(lineno)s - %(message)s',
#	datefmt = "%Y") 	

# add formatter to ch 
ch.setFormatter(formatter)
fh.setFormatter(formatter)

# add ch to logger 
logger.addHandler(ch)
logger.addHandler(fh)

####
import lib.file1


############################### 

# 'application' code 
logger.debug('debug message') 
#logger.info('info message') 
#logger.warning('warn message') 
#logger.error('error message') 
#logger.critical('critical message')


lib.file1.func1()
