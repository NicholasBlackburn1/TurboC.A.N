"""
Drivetrain Data Grabbing
"""


import binascii
import logging


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


def breakPeddleData(data):
   
    obj = int(binascii.hexlify(data[8:10]))
    logging.info("Break Data" + str(obj))
    return int(obj)
    

def inSportManual(data):
    return data[5:6]==b'8'
    
# UwU in sport Mode
def inSport(data):
   
    if data[:2]==b'01':
        return "Sport"
    

def inPark(data):
   return data[5:6]==b'7'

def inReverse(data):
   return data[5:6]==b'6'

def inNetural(data):
    return data[5:6]==b'5'


def inDriveNonSport(data):
    return data[5:6]==b'4'

def inSportFirstGear(data):
    return data[2:4]==b'09'

def inSportSecondGear(data):
    return data[2:4]==b'12'

def gears(data):
    inPark(data) 
    inNetural(data)
    inReverse(data)
    inDriveNonSport(data)
    inSport(data)
