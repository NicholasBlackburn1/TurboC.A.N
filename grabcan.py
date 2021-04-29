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

import numpy
import threading

from src.drivetrain.drivetrain import gasPeddleDataGeneral, steeringWheelDataFine, steeringWheelDataGeneral

name = input("Please enter Driving Tracking log name")
logging.basicConfig(filename="logs/"+str(name)+datetime.now().strftime(
        "%Y_%m_%d-%I_%M_%S_%p_%s")+".log", level=logging.DEBUG)


#check system name, in linux will print 'posix' and in windows will print 'nt'
print("UwU Starting Data caputrue")

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
       logging.info(data[:2])
       logging.info(data[2:4])
       logging.info('SteringWeel FIne data'+ str(steeringWheelDataFine(data)))
       logging.info("Steering Wheel data General:"+" "+str(steeringWheelDataGeneral(data)))
        
    

    if(id == 1041):
      logging.info(data)
      logging.info("gas peddle Data"+"  "+str(gasPeddleDataGeneral(data)))
    
    #logging.debug(str(id) +" "+ str(data))
    if(id == 1040):
        
      
       logging.info("data 1byte set:"+str(data[1]))
       logging.info("data 2byte is gas peddle General Data:"+str(data[2]))
       logging.info("data 3byte is gas peddle Increment Fine data:"+ str(data[3]))
       logging.info("data 4byte set:"+str(data[4]))
       logging.info("data 5byte set:"+str(data[5]))
       logging.info("data 6byte set:"+str(data[6]))
       logging.info("data 7byte set:"+str(data[7]))
       logging.info("data 8byte set:"+str(data[8]))

 
    