""" 
testing canbus ids to see if it works
"""
import binascii
from builtins import print

from cmath import sqrt
from datetime import datetime
import os
import struct
from avro import datafile
import can
import logging
from configparser import ConfigParser
import time 
from src.drivetrain.drivetrain import gasPeddleData, gasPeddleDataGeneral, steeringWheelDataFine, steeringWheelDataGeneral,inPark, breakPeddleData
import src.utils.datafileUwU as uwu


logging.basicConfig(filename="logs/"+datetime.now().strftime(
        "%Y_%m_%d-%I_%M_%S_%p_%s")+".log", level=logging.DEBUG)


#check system name, in linux will print 'posix' and in windows will print 'nt'
print("UwU Starting Data caputrue")



logging.debug("CanBus Starting can network...")
#while True:
can0 = can.interface.Bus(channel = 'can0', bustype = 'socketcan_ctypes')
steeringIndex = 0
GasPeddleIndex = 0

i = 0

for msg in can0:
   
  # This is the vehical d+ata and ids from canbus
  id = int(msg.arbitration_id)
  data = (binascii.hexlify(msg.data))
  
  
  # Steering Wheel Id 
  if(id == 2):
    
      logging.warn("getting Data from Wheel")
      logging.info('SteringWeel FIne data'+ str(steeringWheelDataFine(data)))
      logging.info("Steering Wheel data General:"+" "+str(steeringWheelDataGeneral(data)))
      #createDataFile("Steering",steeringWheelDataGeneral(data),steeringWheelDataFine(data),filename= "UwUWheel.csv",i=steeringIndex)
    
    
  
  # Gas Peddle Id
  if(id == 1040):
      uwu.data(i,data[2],(data[3]))
      i+=1
   
    
    
  # breaks i think
  #if(id == 1300):
    #print ("Can Data from 1300"+ "  "+ "data" +str(data))
  
  #if(id == 117):
    # print("C.A.N BUS 117"+ "  "+ "Data:"+str(data))
#╰─± sudo ip link set can0 type can bitrate 500000               
#╰─± sudo ip link set can0 up        
  #if(id == 1537):
    #print("C.A.N BUS 1537"+ "  "+ "Data:"+str(data))

  #if(id == 1281):
      #print("C.A.N BUS 1281"+ "  "+ "Data:"+str(data))

  """
  # Finds all can ids under 1000
  if(id <= 1000):
    print("ID:"+" "+ str(id)+" "+"DATA:"+" "+str(data)+"\n")
    logging.warn("ID:"+" "+ str(id)+" "+"DATA:"+" "+str(data)+"\n")
  """

  #if(id == 112):
   #   print("ID:"+" "+ str(id)+" "+"DATA:"+" "+str(data)+"\n")
   
  #if(id == 117):
    #print("ID:"+" "+ str(id)+" "+"DATA:"+" "+str(data)+"\n")


  #if(id == 1299):
    #print("ID:"+" "+ str(id)+" "+"DATA:"+" "+str(data)+"\n")
    
  #if(id == 1298):
    #print("ID:"+" "+ str(id)+" "+"DATA:"+" "+str(data)+"\n")
  
  #if(id == 1300):
    #print("ID:"+" "+ str(id)+" "+"DATA:"+" "+str(data)+"\n")

  #if(id == 1297):
   # print("ID:"+" "+ str(id)+" "+"DATA:"+" "+str(data)+"\n")

  #if(id == 1281):
    #print("ID:"+" "+ str(id)+" "+"DATA:"+" "+str(data)+"\n")
  
  #if(id == 1398):
    #print("ID:"+" "+ str(id)+" "+"DATA:"+" "+str(data)+"\n")
  
  #if(id ==1536):
    #print("ID:"+" "+ str(id)+" "+"DATA:"+" "+str(data)+"\n")

  #if(id ==1537):
    #print("ID:"+" "+ str(id)+" "+"DATA:"+" "+str(data)+"\n")
  
  #if(id ==1058):
   #print("ID:"+" "+ str(id)+" "+"DATA:"+" "+str(data)+"\n")
  

  if(id == 1568):
    inPark(data)

  if(id == 1297):
    breakPeddleData(data)

  if(id == 1299):
    print(data)
