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
    channel='can0', bustype='socketcan_ctypes', timeout=1.0)

timetorecordData = 35000  # so ex; 3000 ticks arw secons

i = 0
stearing = 0

breakdex = 0
gas = 0

heartbeat = 0
inGear = None


def save_all_files():
  if inGear:
            
    uwu.Stearingwriter.close()
    
    print("done with file reading stearing file\n")
    logging.warn(str("Stearing Data")+str(uwu.readavroStearing()))

    uwu.gaswriter.close()
    print("done with file reading gass file \n")
    print("gas data \n")
    uwu.readavrogas()
    print(str("Gas Data")+str(uwu.readavrogas()))

    uwu.breakwriter.close()

    print("done with file reading break file \n")
    print("break data \n")
    logging.warn(str("Break Data")+str(uwu.readavrobreak()))




    # Captures Data from my cars canbus and addes to the files
for msg in can0:

    # watch dog for program
    if(msg == None):
        heartbeat += 1

    # Saves all files and exiteds program
    if(heartbeat >= 10):
        logging.critical("WATCHDOG OVER RUN QUITTING PROGRAM and Saving Files")
        save_all_files()
        can0.shutdown()
        logging.debug("good by Program is Ready to die")
        quit()
    else:
        continue

    # if(msg is None or emty): start counting -> if counter  is 10 continue  then reset counter in main code
    # This is the vehical data and ids from canbus

    id = int(msg.arbitration_id)
    data = (binascii.hexlify(msg.data))

    if(id == 1568):
        inGear = inPark(data)
        print(data)
        print("Is car in park?" + str(inGear))

    # Steering Wheel Id
    if(id == 2):

        logging.warn("getting Data from Wheel - > dumping it to the avro file")
        uwu.dumpStearingData(name=str(stearing), datafine=steeringWheelDataFine(data), 
        datagen=steeringWheelDataGeneral(data))

        stearing += 1

    if(id == 1040):
        logging.warn("getting Data from gas - > dumping it to the avro file")
        uwu.dumpGasData(name=str(gas), datafine=data[2], datagen=data[3])
        gas += 1

    if(id == 1297):
        logging.warn("getting Data from break - > dumping it to the avro file")
        uwu.dumpbreakData(name=str(breakdex), data=breakPeddleData(data))
        breakdex += 1


    if(id == 1299):
        pass
