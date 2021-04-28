"""
Drivetrain Data Grabbing
"""


import binascii


# gets data from Steering System and retunds the rounding info
def steeringWheelDataGeneral(data):
    #Data to Ints UwU
    return float(binascii.hexlify(data[2:4]))
#gets Finer Data From Stearing Wheel
def steeringWheelDataFine(data):
    #Data to Ints UwU
    return float(binascii.hexlify(data[:2]))

#gets General Data From Stearing Wheel
def gassPeddleDataGeneral(data):
     #Data to Ints UwU
    pos =float(binascii.hexlify(data[6:8]))
    return pos

def gassPeddleData(data):
     #Data to Ints UwU
    pos =float(binascii.hexlify(data[6]))
    return pos
