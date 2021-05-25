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

i = 0
stearing = 0
breakdex = 0
gas = 0

for msg in can0:
   
  # This is the vehical d+ata and ids from canbus
  id = int(msg.arbitration_id)
  data = (binascii.hexlify(msg.data))
  
  
  # Steering Wheel Id 
  if(id == 2):
    try:
      logging.warn("getting Data from Wheel - > dumping it to the avro file")
      #createDataFile("Steering",steeringWheelDataGeneral(data),steeringWheelDataFine(data),filename= "UwUWheel.csv",i=steeringIndex)
      #uwu.dumpStearingData(i,steeringWheelDataFine(data),steeringWheelDataGeneral(data))
      uwu.dumpStearingData(name=str("stearing"+str(stearing)),datafine=steeringWheelDataFine(data),datagen=steeringWheelDataGeneral(data))
    
      stearing +=1
    
    
      print("i: "+str(stearing))
      if stearing == 3000:
          uwu.Stearingwriter.close()
          
          print("done with file reading break file\n")
          uwu.readavroStearing()
    except:
      print("done captureing Wheel data")
  
  # Gas Peddle Id
  if(id == 1040):
    try:
      logging.warn("getting Data from gas - > dumping it to the avro file")
    #createDataFile("Steering",steeringWheelDataGeneral(data),steeringWheelDataFine(data),filename= "UwUWheel.csv",i=steeringIndex)
    #uwu.dumpStearingData(i,steeringWheelDataFine(data),steeringWheelDataGeneral(data))
      uwu.dumpGasData(name=str("gas"+str(gas)),datafine=data[2],datagen=data[3])
  
      gas +=1


      print("i: "+str(gas))
      if gas == 3000:
          uwu.gaswriter.close()
          
          print("done with file reading break file \n")
          print("gas data \n")
          uwu.readavrogas()
    except:
      print("done capturing Gas")
  
    
    
  # breaks i think
  #if(id == 1300):
    #print ("Can Data from 1300"+ "  "+ "data" +str(data))
  
  #if(id == 117):
    # print("C.A.N BUS 117"+ "  "+ "Data:"+str(data))
        
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
    #uwu.dumpbreakData(str("break"+str(i)),data[5])
    #uwu.breakdata(data,breakdex)
    breakdex +=1

  if(id == 1299):
    pass
 
