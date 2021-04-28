""" 
testing canbus ids to see if it works
"""
import binascii
from builtins import print
from datetime import datetime
import os
import struct
import can
import logging
from configparser import ConfigParser
import time 
import matplotlib.pyplot as plt
import numpy
import drivetrain.drivetrain
    
    
#check system name, in linux will print 'posix' and in windows will print 'nt'
print(os.name)
logging.debug("CanBus Testing starting...")

logging.debug("CanBus Starting can network...")
#while True:
can0 = can.interface.Bus(channel = 'can0', bustype = 'socketcan_ctypes')
for msg in can0:
    
    # This is the vehical data and ids from canbus
    id = int(msg.arbitration_id)
    data = msg.data

    print(drivetrain.drivetrain.steeringWheelData(id,data))
    
    
        