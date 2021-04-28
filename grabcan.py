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
import threading

from src.drivetrain.drivetrain import gasPeddleDataGeneral, steeringWheelDataFine, steeringWheelDataGeneral

logging.basicConfig(filename="logs/"+datetime.now().strftime(
        "%Y_%m_%d-%I_%M_%S_%p_%s")+".log", level=logging.DEBUG)

def update_line(hl, new_data):
    hl.set_xdata(numpy.append(hl.get_xdata(), new_data))
    hl.set_ydata(numpy.append(hl.get_ydata(), new_data))
    plt.draw()


#check system name, in linux will print 'posix' and in windows will print 'nt'
print(os.name)
fig, ax = plt.subplots()
ax.set(xlabel='Rpms i think', ylabel='Active',title='Car Engine Data')

logging.debug("CanBus Testing starting...")

logging.debug("CanBus Starting can network...")
#while True:
can0 = can.interface.Bus(channel = 'can0', bustype = 'socketcan_ctypes')
for msg in can0:
   
    # This is the vehical data and ids from canbus
    id = int(msg.arbitration_id)
    data = (binascii.hexlify(msg.data))
    
    # Steering Wheel Id 
    if(id == 2):
        logging.warn("getting Data from Wheel")
        print(data[:2])
        print(data[2:4])
        print('SteringWeel FIne data'+ str(steeringWheelDataFine(data)))
        print("Steering Wheel data General:"+" "+str(steeringWheelDataGeneral(data)))
        
    

    if(id == 1041):
       print(data)
       print("gas peddle Data"+"  "+str(gasPeddleDataGeneral(data)))
    
    #logging.debug(str(id) +" "+ str(data))
    if(id == 1040):
        
        print(data)
        print("data 1byte set:"+str(data[1]))
        print("data 2byte set:"+str(data[2]))
        #print(data[:2])
        logging.info(str(id) +" "+str(data))


