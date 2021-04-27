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

    
hl, = plt.plot([], [])

def update_line(hl, new_data):
    hl.set_xdata(numpy.append(hl.get_xdata(), new_data))
    hl.set_ydata(numpy.append(hl.get_ydata(), new_data))
    plt.draw()
#check system name, in linux will print 'posix' and in windows will print 'nt'
print(os.name)
logging.debug("CanBus Testing starting...")

logging.debug("CanBus Starting can network...")
#while True:
can0 = can.interface.Bus(channel = 'can0', bustype = 'socketcan_ctypes')
for msg in can0:
    
    # This is the vehical data and ids from canbus
    id = int(msg.arbitration_id)
    data = (binascii.hexlify(msg.data))
    
    #Data to Ints UwU
    steering = int(binascii.hexlify(msg.data[:1]),16)+ int(binascii.hexlify(msg.data[:2]),16)*255/26 
    roundedsteer=round(steering*255/26)
    #print(str(id)+ str(data))
    #print(can0.recv(1))
    if( id == 2):
        print(str(id) +" "+ "data:"+ "     "+ str(round(steering*255/26)))

        if(roundedsteer >=230):
            print("Hello world")
    
        