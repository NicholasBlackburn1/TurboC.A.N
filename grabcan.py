""" 
testing canbus ids to see if it works
"""
import os
import can
import logging
from configparser import ConfigParser
import time 


#check system name, in linux will print 'posix' and in windows will print 'nt'
print(os.name)
logging.debug("CanBus Testing starting...")

logging.debug("CanBus Starting can network...")
#while True:
can0 = can.interface.Bus(channel = 'can0', bustype = 'socketcan_ctypes')
for msg in can0:
    #
    print("{:x}".format(msg.arbitration_id))
    
        