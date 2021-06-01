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

from src.drivetrain.drivetrain import gasPeddleData, gasPeddleDataGeneral, steeringWheelDataFine, steeringWheelDataGeneral, inPark, breakPeddleData
import src.utils.datafileUwU as uwu


logging.basicConfig(filename="logs/"+"s"+".log", level=logging.DEBUG)


# check system name, in linux will print 'posix' and in windows will print 'nt'
print("UwU Starting Data caputrue")


logging.debug("CanBus Starting can network...")
# while True:
can0 = can.interface.Bus(
    channel='can0', bustype='socketcan_ctypes')
notifier = can.Notifier(
    can0, can0, timeout=.5)  # pylint: disable=unused-variable

timetorecordData = 35000  # so ex; 3000 ticks arw secons

i = 0
stearing = 0
rpm =0
breakdex = 0
gas = 0
inc = 0

heartbeat = 0
inGear = None


def save_all_files():
    try:
        uwu.Stearingwriter.close()
        uwu.gaswriter.close()
        uwu.breakwriter.close()
        uwu.rpmwriter.close()
        uwu.Incwriter.close()
    except:
        print("print faild to save")

id = None
data = None

while True:
    msg = can0.recv(timeout=0.5)

 # watch dog for program
    if(msg == None):
        heartbeat += 1
        print("hartbeet:"+str(heartbeat))
    else:
        id = int(msg.arbitration_id)
        data = (binascii.hexlify(msg.data))

    # Saves all files and exiteds program
    if(heartbeat == 10):
        logging.warn("WATCHDOG OVER RUN QUITTING PROGRAM and Saving Files")
        save_all_files()
        logging.debug("good by Program is Ready to die")
        can0.shutdown()
        break
    
    # checks to see if the car is in park
    if(id == 1568):
        inGear = inPark(data)
       
       
        
    #steering Data UwU
    if(id == 2):
        logging.warn("getting Data from Steering - > dumping it to the avro file")
        uwu.dumpStearingData(name=str(stearing),datafine=steeringWheelDataFine(data), datagen=steeringWheelDataGeneral(data))
        stearing += 1

    if(id == 1040):
        logging.warn("getting Data from gas - > dumping it to the avro file")
        uwu.dumpGasData(name=str(gas),datafine=gasPeddleData(data), datagen=gasPeddleDataGeneral(data))
        gas += 1

    # checks the break peddel
    if(id == 1297):
       # print("Break:"+" " + str(breakPeddleData(data)))
        logging.warn("getting Data from break - > dumping it to the avro file")
        uwu.dumpbreakData(name=str(breakdex), data=breakPeddleData(data))
        breakdex += 1

    if(id == 1299):
        pass

    if(id == 1537):
        #print("id 1537:  "+ " "+ str(int(data[7])*10))
       # print ("rpms x1000"+ " "+ str(int(data[7])* 256 + 15/1000))
        # print("Break:"+" " + str(breakPeddleData(data)))
        logging.warn("getting Data from rpm - > dumping it to the avro file")
        uwu.dumprpmData(name=str(rpm), rpm=(int(data[7])),datagen=(int(data[8])))
        rpm += 1

    #if(id > 1000):
      #print(id)

    #if(id == 1300):
     #   print(data)

    #if(id == 112):
     #   print(data)


    #if(id == 1398):
        #nt(data)
    """
    if(id== 1298):
        print("0"+" "+str(data))
        print("1"+" "+str(data[1]))
        print("2"+" "+str(data[2]))
        print("3"+" "+str(data[2]))
        print("4"+" "+str(data[3]))
        print("5"+" "+str(data[4]))
        print("6"+" "+str(data[5]))
        print("7"+" "+str(data[6]))
        print("8"+" "+str(data[7]))
        print("9"+" "+str(data[8]))
        print("10"+" "+str(data[9]))
        print("11"+" "+str(data[10]))
        print("12"+" "+str(data[11]))
        print("13"+" "+str(data[12]))
        print("14"+" "+str(data[13]))
        print("15"+" "+str(data[14]))
        print("16"+" "+str(data[15]))
    """

    if(id == 1281):
        uwu.dumpIncData(inc,data[10],data[11])
        inc +=1
        

