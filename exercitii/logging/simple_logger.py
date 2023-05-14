import logging

# create logger
logger = logging.getLogger('simple_logger')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
#logging.Formatter.__init__(fmt=None, datefmt=None, style='%')
#ORIG
#formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#new - including data formatting
formatter = logging.Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt="%Y-%m-%d %H:%M:%S")

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')
