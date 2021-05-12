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
from src.drivetrain.drivetrain import gasPeddleDataGeneral, steeringWheelDataFine, steeringWheelDataGeneral
from src.utils.datafile import createDataFile, createDataFileid

logging.basicConfig(filename="logs/"+datetime.now().strftime(
        "%Y_%m_%d-%I_%M_%S_%p_%s")+".log", level=logging.DEBUG)


#check system name, in linux will print 'posix' and in windows will print 'nt'
print("UwU Starting Data caputrue")



logging.debug("CanBus Starting can network...")
#while True:
can0 = can.interface.Bus(channel = 'can0', bustype = 'socketcan_ctypes')
steeringIndex = 0
GasPeddleIndex = 0
for msg in can0:
   
    # This is the vehical d+ata and ids from canbus
    id = int(msg.arbitration_id)
    data = (binascii.hexlify(msg.data))
    
    """
    # Steering Wheel Id 
    if(id == 2):
      
       logging.warn("getting Data from Wheel")
       logging.info('SteringWeel FIne data'+ str(steeringWheelDataFine(data)))
       logging.info("Steering Wheel data General:"+" "+str(steeringWheelDataGeneral(data)))
       #createDataFile("Steering",steeringWheelDataGeneral(data),steeringWheelDataFine(data),filename= "UwUWheel.csv",i=steeringIndex)
     
       steeringIndex+=1
    """
    """
    # Gas Peddle Id
    if(id == 1040):
       logging.info("data 1byte set:"+str(data[1]))
       logging.info("data 2byte is gas peddle General Data:"+str(data[2]))
       logging.info("data 3byte is gas peddle Increment Fine data:"+ str(data[3]))
       logging.info("data 4byte set:"+str(data[4]))
       logging.info("data 5byte set:"+str(data[5]))
       logging.info("data 6byte set:"+str(data[6]))
       logging.info("data 7byte set:"+str(data[7]))
       logging.info("data 8byte set:"+str(data[8]))

      
       GasPeddleIndex+=1
    """
   #print(id)
    """
    createDataFileid("Can ids",id,data,filename= "UwUids.csv",i=steeringIndex)
    steeringIndex +=1
    """
    
    # breaks i think
    #if(id == 1300):
      #print ("Can Data from 1300"+ "  "+ "data" +str(data))
    
    #if(id == 117):
      # print("C.A.N BUS 117"+ "  "+ "Data:"+str(data))


    #if(id == 1537):
      #print("C.A.N BUS 1537"+ "  "+ "Data:"+str(data))

    #if(id == 1281):
       #print("C.A.N BUS 1281"+ "  "+ "Data:"+str(data))

    