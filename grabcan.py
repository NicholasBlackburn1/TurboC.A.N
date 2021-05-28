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
from src.drivetrain.drivetrain import gasPeddleData, gasPeddleDataGeneral, steeringWheelDataFine, steeringWheelDataGeneral, inPark, breakPeddleData
import src.utils.datafileUwU as uwu


logging.basicConfig(filename="logs/"+"s"+".log", level=logging.DEBUG)


# check system name, in linux will print 'posix' and in windows will print 'nt'
print("UwU Starting Data caputrue")


logging.debug("CanBus Starting can network...")
# while True:
can0 = can.interface.Bus(
    channel='can0', bustype='socketcan_ctypes')
notifier = can.Notifier(can0, can0,timeout=.5)  # pylint: disable=unused-variable

timetorecordData = 35000  # so ex; 3000 ticks arw secons

i = 0
stearing = 0

breakdex = 0
gas = 0

heartbeat = 0
inGear = None


def save_all_files():
    try:
    
        uwu.breakwriter.close()
        print(str("Break Data File Size:")+" "+str(uwu.readavrobreak()))
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
 

    # if(msg is None or emty): start counting -> if counter  is 10 continue  then reset counter in main code
    # This is the vehical data and ids from canbus

   

    if(id == 1568):
        inGear = inPark(data)
        print(data)
        print("Is car in park?" + str(inGear))

    

    if(id == 1297):
        print("Break:"+" "+ str(breakPeddleData(data)))
        logging.warn("getting Data from break - > dumping it to the avro file")
        uwu.dumpbreakData(name=str(breakdex), data=breakPeddleData(data))
        breakdex += 1


    if(id == 1299):
        pass
