import logging

# create logger
logger = logging.getLogger('simple_logger')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch_s = logging.StreamHandler()
ch_s.setLevel(logging.DEBUG)

class MyHandler(logging.StreamHandler):
    def emit(self, record):
        print("From my handler. record: ", record.msg, record.levelname, record.funcName)
        super().emit(record)

ch = MyHandler()
ch.setLevel(logging.DEBUG)

# create formatter
#logging.Formatter.__init__(fmt=None, datefmt=None, style='%')
#ORIG
#formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#new - including data formatting
formatter = logging.Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(funcName)s', datefmt="%Y-%m-%d %H:%M:%S")

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

# 'application' code
logger.debug('my debug message')
logger.info('my info message')
logger.warning('my warn message')
logger.error('my error message')
logger.critical('my critical message')


def myFunc1():
    logger.debug('my debug message')
    
myFunc1()
