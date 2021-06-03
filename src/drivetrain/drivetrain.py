"""
Drivetrain Data Grabbing
"""


import binascii
import logging
import gpiozero

# gets data from Steering System and retunds the rounding info
def steeringWheelDataGeneral(data):
    #Data to Ints UwU
    return int(binascii.hexlify(data[2:4]))
#gets Finer Data From Stearing Wheel
def steeringWheelDataFine(data):
    #Data to Ints UwU
    return int(binascii.hexlify(data[:2]))

#gets General Data From Stearing Wheel
def gasPeddleDataGeneral(data):
     #Data to Ints UwU
    pos =data[2]
    return pos

def gasPeddleData(data):
     #Data to Ints UwU
   # print(data[3])
    pos =data[3]
    return pos

def inPark(data):
    
    if(data[5] == 53):
     
      return True
    else:
        return False
   

def breakPeddleData(data):
   
    obj = int(binascii.hexlify(data[8:10]))
    logging.info("Break Data" + str(obj))
    return int(obj)
    