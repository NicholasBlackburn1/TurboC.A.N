"""
Drivetrain Data Grabbing
"""


import binascii


# gets data from Steering System and retunds the rounding info
def steeringWheelData(id,data):
    #Data to Ints UwU
    if(id == 2):
        steering = int(binascii.hexlify(data[:1]),16)+ int(binascii.hexlify(data[:2]),16)*255/26 
        return steering


def gassPeddleData(id,data):
     #Data to Ints UwU
    if(id == 1041):
        gas = int(binascii.hexlify(data[:3]),16)+ int(binascii.hexlify(data[:4]),16)*255/26 
        return gas