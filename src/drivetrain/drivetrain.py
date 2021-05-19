"""
Drivetrain Data Grabbing
"""


import binascii
import gpiozero

# gets data from Steering System and retunds the rounding info
def steeringWheelDataGeneral(data):
    #Data to Ints UwU
    return float(binascii.hexlify(data[2:4]))
#gets Finer Data From Stearing Wheel
def steeringWheelDataFine(data):
    #Data to Ints UwU
    return float(binascii.hexlify(data[:2]))

#gets General Data From Stearing Wheel
def gasPeddleDataGeneral(data):
     #Data to Ints UwU
    pos =float(binascii.hexlify(data[2]))
    return pos

def gasPeddleData(data):
     #Data to Ints UwU
    pos =float(binascii.hexlify(data[3]))
    return pos

def inPark(data,led):
    if(data[5] == 53):
      led.on()
    else:
      led.off()



def inGear(data,led):
    if(data[5] == 53):
      led.off()
    else:
      led.on()

def breakPeddleData(data):
    return binascii.hexlify(data[5])
