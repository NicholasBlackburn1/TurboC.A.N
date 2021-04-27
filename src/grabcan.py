""" 
testing canbus ids to see if it works
"""
import binascii
import os
import struct
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
    
    data = (binascii.hexlify(msg.data), 16)
    id = int(msg.arbitration_id)



    print (str(id) + "data:"+ str(data))
    
        