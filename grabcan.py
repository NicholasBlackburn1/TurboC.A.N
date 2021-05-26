""" 
testing canbus ids to see if it works
#╰─± sudo ip link set can0 type can bitrate 500000               
#╰─± sudo ip link set can0 up
"""
import binascii
from builtins import print

from cmath import sqrt
from datetime import datetime
import os
import struct
from xmlrpc.client import DateTime
from avro import datafile
import can
import logging
from configparser import ConfigParser
import time

from sqlalchemy import false 
from src.drivetrain.drivetrain import gasPeddleData, gasPeddleDataGeneral, steeringWheelDataFine, steeringWheelDataGeneral,inPark, breakPeddleData
import src.utils.datafileUwU as uwu


logging.basicConfig(filename="logs/"+"s"+".log", level=logging.DEBUG)


#check system name, in linux will print 'posix' and in windows will print 'nt'
print("UwU Starting Data caputrue")



logging.debug("CanBus Starting can network...")
#while True:
can0 = can.interface.Bus(channel = 'can0', bustype = 'socketcan_ctypes')

timetorecordData = 35000 # so ex; 3000 ticks arw secons

i = 0
stearing = 0
breakdex = 0
gas = 0


inGear = None
# Captures Data from my cars canbus and addes to the files 
for msg in can0:
   
  # This is the vehical d+ata and ids from canbus
  id = int(msg.arbitration_id)
  data = (binascii.hexlify(msg.data))

  if(id == 1568):
    inGear = inPark(data) 
    print(data)
    print("Is car in park?"+ str(inGear))

  # Steering Wheel Id 
  if(id == 2):
      try:
        logging.warn("getting Data from Wheel - > dumping it to the avro file")
        uwu.dumpStearingData(name=str(stearing),datafine=steeringWheelDataFine(data),datagen=steeringWheelDataGeneral(data))
      
        stearing +=1
      
        if stearing < timetorecordData:
          #print("StearingIndex: "+str(stearing))
           pass
        if inGear:
            
            uwu.Stearingwriter.close()
            
            print("done with file reading break file\n")
            logging.warn(str("Stearing Data")+str(uwu.readavroStearing()))
      except:
        print("done captureing Wheel data")
        uwu.Stearingwriter.close()

  
  if(id == 1040):
    try:
        logging.warn("getting Data from gas - > dumping it to the avro file")
        uwu.dumpGasData(name=str(gas),datafine=data[2],datagen=data[3])
        
    
        gas +=1

        if(gas < timetorecordData):
          #print("gasIndex: "+str(gas))
          pass
        if inGear:
            uwu.gaswriter.close()
            
            print("done with file reading break file \n")
            print("gas data \n")
            uwu.readavrogas()
            print(str("Gas Data")+str(uwu.readavrogas()))
    except:
        print("done capturing Gas")
        uwu.gaswriter.flush()


  
 

  if(id == 1297):
      try:
            logging.warn("getting Data from break - > dumping it to the avro file")
            uwu.dumpbreakData(name=str(breakdex),data=breakPeddleData(data))
        
            breakdex+=1

            if(breakdex < timetorecordData):
              #print("breakIndex: "+str(breakdex))
              pass
            if inGear:
                uwu.breakwriter.close()
                
                print("done with file reading break file \n")
                print("break data \n")
                logging.warn(str("Break Data")+str(uwu.readavrobreak()))
      except:
            print("done capturing break")
            uwu.breakwriter.close()
            



  if(id == 1299):
    pass

 

  if(msg == None or b''):
    break