""" 
testing canbus ids to see if it works
"""
import binascii
from builtins import print
from cmath import sqrt
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


# gets data from Steering System and retunds the rounding info
def steeringWheelDataGeneral(id,data):
    #Data to Ints UwU
    return float(binascii.hexlify(data[2:4]))

def steeringWheelDataFine(id,data):
    #Data to Ints UwU
    return float(binascii.hexlify(data[:2]))


def gassPeddleData(id,data):
     #Data to Ints UwU
    pos =float(binascii.hexlify(data[6:8]))*255/25
    return pos

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
    
    if(id == 2):
        print(data[:2])
        print(data[2:4])
        print('SteringWeel FIne data'+ str(steeringWheelDataFine(id,data)))
        print("Steering Wheel data General:"+" "+str(steeringWheelDataGeneral(id,data)))

    '''     
    if(id == 1041):
       print("rounded data:" +str(round(gassPeddleData(id,data))))
       print("gas peddle Data"+"  "+str(gassPeddleData(id,data)))
    '''
        