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
notifier = can.Notifier(
    can0, can0, timeout=.5)  # pylint: disable=unused-variable

timetorecordData = 35000  # so ex; 3000 ticks arw secons

i = 0
stearing = 0

breakdex = 0
gas = 0

heartbeat = 0
inGear = None


def save_all_files():
    try:
        uwu.Stearingwriter.close()
        uwu.gaswriter.close()
        uwu.breakwriter.close()
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
        print(data)
        print("Is car in park?" + str(inGear))
    
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
        print("Break:"+" " + str(breakPeddleData(data)))
        logging.warn("getting Data from break - > dumping it to the avro file")
        uwu.dumpbreakData(name=str(breakdex), data=breakPeddleData(data))
        breakdex += 1

    if(id == 1299):
        pass
